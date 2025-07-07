# encoding: utf-8
"""
Various functions for applying Fast Approximate Anti-Aliasing (FXAA) to Pygame-CE surfaces.

Due to the nature of FXAA, results may be perceived as blurry or soft.
"""

from typing import Union, Literal

import numpy as np
import pygame as pg

from ._common import compute_luma

assert getattr(pg, "IS_CE", False), (
    "This module is designed to work with Pygame-CE (Pygame Community Edition) only."
)


def fxaa(
    surf: pg.Surface,
    threshold: Union[int, float] = 20,
    diagonal_blur: bool = False,
    luma: Literal["rec709", "rec601", "rec2100", "mean"] = "mean",
    f4: bool = False,
) -> pg.Surface:
    """
    :param luma: str ("rec709", "rec601", "rec2100", "mean")
    :param diagonal_blur: bool
    :param threshold: float or int
    :param surf: pygame.Surface:
    :param f4: bool:
    :return: pygame.Surface:
    """

    assert isinstance(surf, pg.Surface)
    assert isinstance(threshold, (int, float))
    assert threshold > 0
    assert isinstance(f4, bool)

    array = pg.surfarray.array3d(surf).astype(
        np.float32 if not f4 else np.float64
    )

    gray = compute_luma(array, luma)

    dx = np.abs(np.roll(gray, -1, axis=0) - gray)
    dy = np.abs(np.roll(gray, -1, axis=1) - gray)
    dxy1 = np.abs(np.roll(np.roll(gray, -1, axis=0), -1, axis=1) - gray)
    dxy2 = np.abs(np.roll(np.roll(gray, -1, axis=0), 1, axis=1) - gray)
    edge_strength = dx + dy + dxy1 + dxy2

    edge_mask = (edge_strength > threshold).astype(
        np.float32 if not f4 else np.float64
    )[..., np.newaxis]

    # Directional box blur
    blurred = (
        np.roll(array, 1, axis=0)
        + np.roll(array, -1, axis=0)
        + np.roll(array, 1, axis=1)
        + np.roll(array, -1, axis=1)
    ) / 4.0

    # diagonal blur if enabled
    if diagonal_blur:
        blurred += (
            np.roll(np.roll(array, 1, axis=0), 1, axis=1)
            + np.roll(np.roll(array, -1, axis=0), -1, axis=1)
        ) / 6.0

    result = array * (1.0 - edge_mask) + blurred * edge_mask
    result = np.clip(result, 0, 255).astype(np.uint8)

    return pg.surfarray.make_surface(result)


def fxaa_hq(
    surf: pg.Surface,
    threshold: Union[int, float] = 10,
    diagonal_blur: bool = True,
    luma: Literal["rec709", "rec601", "rec2100", "mean"] = "rec709",
    f4: bool = True,
) -> pg.Surface:
    """
    :param luma: str ("rec709", "rec601", "rec2100", "mean")
    :param diagonal_blur: bool
    :param threshold: float or int
    :param surf: pygame.Surface:
    :param f4: bool:
    :return: pygame.Surface:
    """
    return fxaa(surf, threshold, diagonal_blur, luma, f4)


def fxaa311(
    surf: pg.Surface,
    threshold: Union[int, float] = 0.05,
    diagonal_blur: bool = True,
    luma: Literal["rec709", "rec601", "rec2100", "mean"] = "rec2100",
    f4: bool = False,
) -> pg.Surface:
    """
    :param luma: str ("rec709", "rec601", "rec2100", "mean")
    :param diagonal_blur: bool
    :param threshold: float or int
    :param surf: pygame.Surface:
    :param f4: bool:
    :return: pygame.Surface:
    """

    assert isinstance(surf, pg.Surface)
    assert isinstance(threshold, (int, float))
    assert threshold > 0
    assert isinstance(f4, bool)

    array = pg.surfarray.array3d(surf).astype(
        np.float32 if not f4 else np.float64
    )

    gray = compute_luma(array, luma)

    # Edge detection in 4 directions
    dx = np.abs(np.roll(gray, -1, axis=0) - gray)
    dy = np.abs(np.roll(gray, -1, axis=1) - gray)
    dxy1 = np.abs(np.roll(np.roll(gray, -1, axis=0), -1, axis=1) - gray)
    dxy2 = np.abs(np.roll(np.roll(gray, -1, axis=0), 1, axis=1) - gray)

    edge_strength = dx + dy + dxy1 + dxy2

    # Adaptive thresholding due to FXAA3.11
    adaptive_thresh = np.maximum(threshold, 0.0833 * np.std(gray))
    edge_mask = (edge_strength > adaptive_thresh * 255).astype(
        np.float32 if not f4 else np.float64
    )[..., np.newaxis]

    blurred = (
        np.roll(array, 1, axis=0)
        + np.roll(array, -1, axis=0)
        + np.roll(array, 1, axis=1)
        + np.roll(array, -1, axis=1)
    ) / 4.0

    # diagonal blur if enabled
    if diagonal_blur:
        blurred += (
            np.roll(np.roll(array, 1, axis=0), 1, axis=1)
            + np.roll(np.roll(array, -1, axis=0), -1, axis=1)
        ) / 6.0

    result = array * (1.0 - edge_mask) + blurred * edge_mask
    result = np.clip(result, 0, 255).astype(np.uint8)

    return pg.surfarray.make_surface(result)


# Aliases
fxaa_default = legacy_fxaa = fxaa_legacy = fxaa
fxaa_3_11 = fxaa_311 = modern_fxaa = fxaa_modern = fxaa311
fxaa_high_quality = fxaa_highquality = fxaa_hq
