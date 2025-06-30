# encoding: utf-8

"""Scharr Normal Filter Anti-Aliasing for Pygame-CE surfaces."""

import pygame as pg
import numpy as np


def scharr_nfaa(
    surf: pg.Surface, threshold: float, strength: float, f4: bool = False
) -> pg.Surface:
    array = pg.surfarray.array3d(surf).astype(
        np.float32 if not f4 else np.float64
    )
    h, w = array.shape[:2]

    luma = (
        array[..., 0] * 0.2126
        + array[..., 1] * 0.7152
        + array[..., 2] * 0.0722
    )

    kx = np.array(
        [
            [3, 0, -3],
            [10, 0, -10],
            [3, 0, -3],
        ],
        dtype=np.float32 if not f4 else np.float64,
    )
    ky = np.array(
        [
            [3, 10, 3],
            [0, 0, 0],
            [-3, -10, -3],
        ],
        dtype=np.float32 if not f4 else np.float64,
    )

    def convolve2d(img, kernel):
        out = np.zeros_like(img)
        padded = np.pad(img, 1, mode="edge")
        for y in range(h):
            for x in range(w):
                region = padded[y : y + 3, x : x + 3]
                out[y, x] = np.sum(region * kernel)
        return out

    dx = convolve2d(luma, kx)
    dy = convolve2d(luma, ky)

    magnitude = np.sqrt(dx**2 + dy**2)
    norm = np.stack([-dy, dx], axis=-1)

    norm_len = np.clip(
        np.linalg.norm(norm, axis=-1, keepdims=True), 1e-6, None
    )
    norm_unit = norm / norm_len

    coords = (
        np.indices((h, w))
        .transpose(1, 2, 0)
        .astype(np.float32 if not f4 else np.float64)
    )
    offset = norm_unit * 1.0

    p1 = np.clip(coords + offset, [0, 0], [h - 1, w - 1]).astype(np.int32)
    p2 = np.clip(coords - offset, [0, 0], [h - 1, w - 1]).astype(np.int32)

    blurred = (
        array + array[p1[..., 0], p1[..., 1]] + array[p2[..., 0], p2[..., 1]]
    ) / 3.0

    edge_mask = (magnitude > threshold * 255).astype(
        np.float32 if not f4 else np.float64
    )[..., None]
    result = array * (1 - edge_mask * strength) + blurred * (
        edge_mask * strength
    )
    result = np.clip(result, 0, 255).astype(np.uint8)

    return pg.surfarray.make_surface(result)
