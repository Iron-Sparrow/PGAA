# encoding: utf-8

"""Scharr Normal Filter Anti-Aliasing for Pygame-CE surfaces."""

from typing import Literal

import numpy as np
import pygame as pg

from ._common import compute_luma


def scharr_nfaa(
    surf: pg.Surface,
    threshold: float,
    strength: float,
    luma: Literal["rec601", "rec709", "rec2100", "mean"] = "rec709",
    f4: bool = False,
) -> pg.Surface:
    """
    Applies Scharr's Normal Map and the uses it to perform Normal Filter Anti-Aliasing.
    :param surf: pygame.Surface:
    :param threshold: float:
    :param strength: float:
    :param f4: bool:
    :return: pygame.Surface:
    """
    assert isinstance(surf, pg.Surface)
    assert isinstance(threshold, float) and threshold >= 0
    assert 0 <= strength <= 1 and isinstance(strength, float)
    assert isinstance(f4, bool)

    array = pg.surfarray.array3d(surf).astype(
        np.float32 if not f4 else np.float64
    )
    h, w = array.shape[:2]

    luminance = compute_luma(array, luma)

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
        """
        :param img:
        :param kernel:
        :return:
        """
        out = np.zeros_like(img)
        padded = np.pad(img, 1, mode="edge")
        for y in range(h):
            for x in range(w):
                region = padded[y : y + 3, x : x + 3]
                out[y, x] = np.sum(region * kernel)
        return out

    dx = convolve2d(luminance, kx)
    dy = convolve2d(luminance, ky)

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


def scharr_nfaa_low(surf: pg.Surface, f4: bool = False) -> pg.Surface:
    """
    :param surf:
    :param f4:
    :return:
    """
    return scharr_nfaa(surf, 0.2, 0.3, "rec709", f4)


def scharr_nfaa_medium(surf: pg.Surface, f4: bool = False) -> pg.Surface:
    """
    :param surf:
    :param f4:
    :return:
    """
    return scharr_nfaa(surf, 0.1, 0.6, "rec709", f4)


def scharr_nfaa_high(surf: pg.Surface, f4: bool = True) -> pg.Surface:
    """
    :param surf:
    :param f4:
    :return:
    """
    return scharr_nfaa(surf, 0.05, 0.85, "rec709", f4)


# very high quality is simply replaced with ultra for simpler syntax and linguistics


def scharr_nfaa_ultra(surf: pg.Surface, f4: bool = True) -> pg.Surface:
    """
    :param surf:
    :param f4:
    :return:
    """
    return scharr_nfaa(surf, 0.025, 1.0, "rec709", f4)


# Aliases
scharr_nfaa_lq = scharr_nfaa_low_quality = scharr_nfaa_low
scharr_nfaa_default = scharr_nfaa_mq = scharr_nfaa_medium_quality = (
    scharr_nfaa_medium
)
scharr_nfaa_high_quality = scharr_nfaa_hq = scharr_nfaa_high
scharr_nfaa_ultra_quality = scharr_nfaa_ultra_high_quality = (
    scharr_nfaa_uq
) = scharr_nfaa_uhq = scharr_nfaa_ultra
