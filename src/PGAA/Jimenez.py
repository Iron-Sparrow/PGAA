"""
Jimenez's MLAA is the precursor to the Subpixel Morphological Antialiasing (SMAA) algorithm.
It was built atop of Reshetov's MLAA algorithm.
"""

import pygame as pg
import numpy as np
from typing import Union, Literal


def jimenez_mlaa(
    surf: pg.Surface,
    threshold: Union[float, int] = 20,
    max_search: int = 8,
    f4: bool = False,
) -> pg.Surface:
    """
    :param surf: pygame.Surface:
    :param threshold: float or int:
    :param max_search: int:
    :param f4: bool:
    :return: pygame.Surface:
    """

    assert isinstance(surf, pg.Surface)
    assert isinstance(threshold, (int, float))
    assert isinstance(max_search, int) and max_search > 0
    assert isinstance(f4, bool)

    array = pg.surfarray.array3d(surf).astype(
        np.float32 if not f4 else np.float64
    )
    h, w = array.shape[:2]
    # Compute accurate luminance (Rec. 709)
    luma = (
        array[..., 0] * 0.2126
        + array[..., 1] * 0.7152
        + array[..., 2] * 0.0722
    )

    # Edge Detection booleans
    e_h = np.abs(np.roll(luma, -1, axis=0) - luma) > threshold
    e_v = np.abs(np.roll(luma, -1, axis=1) - luma) > threshold
    e_d1 = (
        np.abs(np.roll(np.roll(luma, -1, axis=0), -1, axis=1) - luma)
        > threshold
    )
    e_d2 = (
        np.abs(np.roll(np.roll(luma, -1, axis=0), 1, axis=1) - luma)
        > threshold
    )

    edge_map = np.logical_or.reduce((e_h, e_v, e_d1, e_d2)).astype(np.uint8)

    # Build shape rejection mask
    reject_mask = np.zeros_like(edge_map)

    patterns = [
        np.array([[1, 0, 0], [1, 0, 0], [0, 0, 0]]),  # L
        np.array([[0, 1, 0], [1, 1, 1], [0, 0, 0]]),  # T
        np.array([[1, 0, 1], [0, 1, 0], [0, 0, 0]]),  # U
    ]

    for y in range(1, h - 1):
        for x in range(1, w - 1):
            patch = edge_map[y - 1 : y + 2, x - 1 : x + 2]
            for pat in patterns:
                for rot in range(4):
                    if np.array_equal(patch, np.rot90(pat, k=rot)):
                        reject_mask[y, x] = 1
                        break

    reject_mask = reject_mask[..., np.newaxis].astype(np.float32)

    # Corner suppression
    is_corner = ((e_h & e_v) | (e_d1 & e_d2))[..., np.newaxis].astype(
        np.float32
    )

    def compute_weights(
        mask: np.ndarray,
        direction: Literal["down", "right", "diag1", "diag2"],
    ) -> np.ndarray:
        assert direction in ["down", "right", "diag1", "diag2"], (
            "Invalid direction specified for compute_weights."
        )

        accum = np.zeros_like(
            mask, dtype=np.float32 if not f4 else np.float64
        )
        for i in range(1, max_search + 1):
            if direction == "down":
                shifted = np.roll(mask, -i, axis=0)
            elif direction == "right":
                shifted = np.roll(mask, -i, axis=1)
            elif direction == "diag1":
                shifted = np.roll(np.roll(mask, -i, axis=0), -i, axis=1)
            elif direction == "diag2":
                shifted = np.roll(np.roll(mask, -i, axis=0), i, axis=1)
            else:
                raise ValueError(
                    "Invalid direction specified for compute_weights."
                )
            accum += shifted
        return np.clip(accum / max_search, 0.0, 1.0)[..., np.newaxis]

    w_h = compute_weights(e_h, "down")
    w_v = compute_weights(e_v, "right")
    w_d1 = compute_weights(e_d1, "diag1")
    w_d2 = compute_weights(e_d2, "diag2")

    blend = (
        np.roll(array, 1, axis=0) * w_h
        + np.roll(array, -1, axis=0) * w_h
        + np.roll(array, 1, axis=1) * w_v
        + np.roll(array, -1, axis=1) * w_v
        + np.roll(np.roll(array, -1, axis=0), -1, axis=1) * w_d1
        + np.roll(np.roll(array, -1, axis=0), 1, axis=1) * w_d2
    )

    total_weight = w_h * 2 + w_v * 2 + w_d1 + w_d2
    total_weight = np.clip(
        total_weight * (1.0 - is_corner) * (1.0 - reject_mask), 0.0, 1.0
    )

    result = array * (1.0 - total_weight) + blend
    result = np.clip(result, 0, 255).astype(np.uint8)

    return pg.surfarray.make_surface(result)


def jimenez_mlaa_low(
    surf: pg.Surface,
    threshold: Union[float, int] = 30,
    max_search: int = 4,
    f4: bool = False,
) -> pg.Surface:
    """
    :param surf: pygame.Surface:
    :param threshold: float or int:
    :param max_search: int:
    :param f4: bool:
    :return: pygame.Surface:
    """
    return jimenez_mlaa(surf, threshold, max_search, f4)


def jimenez_mlaa_high(
    surf: pg.Surface,
    threshold: Union[float, int] = 10,
    max_search: int = 16,
    f4: bool = True,
) -> pg.Surface:
    """
    :param surf: pygame.Surface:
    :param threshold: float or int:
    :param max_search: int:
    :param f4: bool:
    :return: pygame.Surface:
    """
    return jimenez_mlaa(surf, threshold, max_search, f4)


def jimenez_mlaa_very_high(
    surf: pg.Surface,
    threshold: Union[float, int] = 5,
    max_search: int = 32,
    f4: bool = True,
) -> pg.Surface:
    """
    :param surf: pygame.Surface:
    :param threshold: float or int:
    :param max_search: int:
    :param f4: bool:
    :return: pygame.Surface:
    """
    return jimenez_mlaa(surf, threshold, max_search, f4)


# Aliases
smaa15_default = jimenez_default = jimenez_mlaa_default = smaa15 = (
    jimenez_mlaa_medium
) = jimenez_medium = jimenez_mq = jimenez_medium_quality = (
    jimenez_mlaa_medium_quality
) = jimenez_mlaa_mq = jimenez_mlaa
smaa15_high = jimenez_high = jimenez_mlaa_high
smaa15_very_high = jimenez_very_high = jimenez_mlaa_very_high
