"""
Various functions for applying Fast Approximate Anti-Aliasing (FXAA) to Pygame-CE surfaces.
"""

import pygame as pg
import numpy as np
from typing import Union

assert getattr(pg, "IS_CE", False), (
    "This module is designed to work with Pygame-CE (Pygame Community Edition) only."
)


def fxaa(
    surf: pg.Surface, threshold: Union[int, float] = 20, f4: bool = False
) -> pg.Surface:
    """
    :param surf: pygame.Surface:
    :param f4: bool:
    :return: pygame.Surface:
    """

    assert isinstance(surf, pg.Surface)
    assert isinstance(threshold, (int, float))
    assert isinstance(f4, bool)

    array = pg.surfarray.array3d(surf).astype(
        np.float32 if not f4 else np.float64
    )

    gray = np.mean(array, axis=2)

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

    result = array * (1.0 - edge_mask) + blurred * edge_mask
    result = np.clip(result, 0, 255).astype(np.uint8)

    return pg.surfarray.make_surface(result)


def fxaa_hq(
    surf: pg.Surface, threshold: Union[int, float] = 10, f4: bool = True
) -> pg.Surface:
    """
    :param surf: pygame.Surface:
    :param f4: bool:
    :return: pygame.Surface:
    """

    assert isinstance(surf, pg.Surface)
    assert isinstance(threshold, (int, float))
    assert isinstance(f4, bool)

    array = pg.surfarray.array3d(surf).astype(
        np.float32 if not f4 else np.float64
    )

    gray = np.mean(array, axis=2)

    dx = np.abs(np.roll(gray, -1, axis=0) - gray)
    dy = np.abs(np.roll(gray, -1, axis=1) - gray)
    dxy1 = np.abs(np.roll(np.roll(gray, -1, axis=0), -1, axis=1) - gray)
    dxy2 = np.abs(np.roll(np.roll(gray, -1, axis=0), 1, axis=1) - gray)
    edge_strength = dx + dy + dxy1 + dxy2

    edge_mask = edge_strength > threshold

    blurred = (
        np.roll(array, 1, axis=0)
        + np.roll(array, -1, axis=0)
        + np.roll(array, 1, axis=1)
        + np.roll(array, -1, axis=1)
    ) / 4.0

    result = array * (1.0 - edge_mask) + blurred * edge_mask
    result = np.clip(result, 0, 255).astype(np.uint8)

    return pg.surfarray.make_surface(result)


def fxaa311(
    surf: pg.Surface, threshold: Union[int, float] = 0.05, f4: bool = False
) -> pg.Surface:
    """
    :param surf: pygame.Surface:
    :param f4: bool:
    :return: pygame.Surface:
    """

    assert isinstance(surf, pg.Surface)
    assert isinstance(threshold, (int, float))
    assert isinstance(f4, bool)

    array = pg.surfarray.array3d(surf).astype(
        np.float32 if not f4 else np.float64
    )
    # Rec. 709 weights
    gray = (
        array[..., 0] * 0.2126
        + array[..., 1] * 0.7152
        + array[..., 2] * 0.0722
    )

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

    result = array * (1.0 - edge_mask) + blurred * edge_mask
    result = np.clip(result, 0, 255).astype(np.uint8)

    return pg.surfarray.make_surface(result)


# Aliases
fxaa_default = legacy_fxaa = fxaa_legacy = fxaa
fxaa_3_11 = modern_fxaa = fxaa_modern = fxaa311
fxaa_high_quality = fxaa_highquality = fxaa_hq
