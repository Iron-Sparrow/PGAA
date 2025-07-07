# encoding: utf-8
"""
Jimenez's MLAA is the precursor to the Subpixel Morphological Antialiasing (SMAA) algorithm.
It was built atop of Reshetov's MLAA algorithm.
"""

from typing import Union, Literal

import numpy as np
import pygame as pg

from ._common import compute_luma

assert getattr(pg, "IS_CE", False), (
    "This module is designed to work with Pygame-CE (Pygame Community Edition) only."
)

if __debug__:
    print(
        "Using Jimenez's MLAA algorithm is strongly discouraged for SMAA is the successor with better results."
        "Please, import SMAA from SubpixelMorphological."
    )


def jimenez_mlaa(
    surf: pg.Surface,
    threshold: Union[float, int],
    max_search: int,
    luma: Literal["rec709", "rec601", "rec2100", "mean"] = "rec709",
    f4: bool = False,
) -> pg.Surface:
    """
    Applies Jimenez-MLAA to the given surface and returns a new surface with anti-aliasing applied.
    :param luma:
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

    luminance = compute_luma(array, luma)

    # Edge Detection booleans
    e_h = np.abs(np.roll(luminance, -1, axis=0) - luminance) > threshold
    e_v = np.abs(np.roll(luminance, -1, axis=1) - luminance) > threshold
    e_d1 = (
        np.abs(
            np.roll(np.roll(luminance, -1, axis=0), -1, axis=1) - luminance
        )
        > threshold
    )
    e_d2 = (
        np.abs(np.roll(np.roll(luminance, -1, axis=0), 1, axis=1) - luminance)
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
    f4: bool = False,
) -> pg.Surface:
    """
    Wrapper for the low quality Jimenez-MLAA.
    :param surf: pygame.Surface:
    :param f4: bool:
    :return: pygame.Surface:
    """
    return jimenez_mlaa(surf, 30, 4, "rec709", f4)


def jimenez_mlaa_medium(surf, f4: bool = False) -> pg.Surface:
    """
    Wrapper for the medium quality Jimenez-MLAA.
    :param surf: pygame.Surface:
    :param f4: bool:
    :return: pygame.Surface:
    """
    return jimenez_mlaa(surf, 20, 8, "rec709", f4)


def jimenez_mlaa_high(
    surf: pg.Surface,
    f4: bool = True,
) -> pg.Surface:
    """
    Wrapper for the high quality Jimenez-MLAA.
    :param surf: pygame.Surface:
    :param f4: bool:
    :return: pygame.Surface:
    """
    return jimenez_mlaa(surf, 10, 16, "rec709", f4)


def jimenez_mlaa_very_high(
    surf: pg.Surface,
    f4: bool = True,
) -> pg.Surface:
    """
    Wrapper for the very high quality Jimenez-MLAA.
    :param surf: pygame.Surface:
    :param f4: bool:
    :return: pygame.Surface:
    """
    return jimenez_mlaa(surf, 5, 32, "rec709", f4)


# Aliases
smaa15_default = smaa15_mq = jimenez_default = jimenez_mlaa_default = (
    jimenez_medium
) = jimenez_mq = jimenez_medium_quality = jimenez_mlaa_medium_quality = (
    jimenez_mlaa_mq
) = jimenez_mlaa_medium
smaa15_high = smaa15_hq = jimenez_high = jimenez_high_quality = (
    jimenez_mlaa_high_quality
) = jimenez_hq = jimenez_mlaa_hq = jimenez_mlaa_high
smaa15_very_high = smaa15_very_hq = smaa15_very_high_quality = smaa15_vhq = (
    jimenez_very_high
) = jimenez_very_hq = jimenez_very_high_quality = (
    jimenez_mlaa_very_high_quality
) = jimenez_mlaa_vhq = jimenez_mlaa_very_hq = jimenez_mlaa_very_high
