"""
Functions for applying various forms of Morphological Anti-Aliasing (MLAA) to Pygame-CE surfaces.
"""

import pygame as pg
import numpy as np
from typing import Union, Literal


def mlaa_low(surf: pg.Surface, f4: bool = False) -> pg.Surface:
    """
    :param surf: pygame.Surface: The surface to apply low-quality MLAA to.
    :param f4: bool: If True, use float64 for calculations; otherwise, use float32.
    :return: pygame.Surface: A new surface with low-quality MLAA applied.
    """
    assert isinstance(surf, pg.Surface)
    assert isinstance(f4, bool)

    array = pg.surfarray.array3d(surface=surf).astype(
        np.float32 if not f4 else np.float64
    )
    gray = np.mean(array, axis=2)

    diff_x = np.abs(np.diff(gray, axis=0, append=gray[-1:]))
    diff_y = np.abs(np.diff(gray, axis=1, append=gray[:, -1:]))

    edge_mask = ((diff_x + diff_y) > 60).astype(
        np.float32 if not f4 else np.float64
    )[..., np.newaxis]

    kernel_1d = np.ones(3, dtype=(np.float32 if not f4 else np.float64)) / 3
    smooth_x = np.apply_along_axis(
        lambda m: np.convolve(m, kernel_1d, mode="same"), axis=0, arr=array
    )
    smooth_y = np.apply_along_axis(
        lambda m: np.convolve(m, kernel_1d, mode="same"), axis=1, arr=array
    )
    avg = (smooth_x + smooth_y) / 2

    result = array * (1 - edge_mask * 0.4) + avg * edge_mask * 0.4
    result = np.clip(result, 0, 255).astype(np.uint8)

    return pg.surfarray.make_surface(result)


def mlaa_medium(surf: pg.Surface, f4: bool = False) -> pg.Surface:
    """
    :param surf: pygame.Surface: Surface to apply medium-quality MLAA to.
    :param f4: bool: If True, use float64 for calculations; otherwise, use float32.
    :return: pygame.Surface: A new surface with medium-quality MLAA applied.
    """
    assert isinstance(surf, pg.Surface)
    assert isinstance(f4, bool)
    array = pg.surfarray.array3d(surface=surf).astype(
        np.float32 if not f4 else np.float64
    )
    gray = np.mean(array, axis=2)

    diff_x = np.abs(np.diff(gray, axis=0, append=gray[-1:]))
    diff_y = np.abs(np.diff(gray, axis=1, append=gray[:, -1:]))
    edge_mask = ((diff_x + diff_y) > 40).astype(
        np.float32 if not f4 else np.float64
    )[..., np.newaxis]

    kernel_1d = np.ones(5, dtype=(np.float32 if not f4 else np.float64)) / 5
    smooth_x = np.apply_along_axis(
        lambda m: np.convolve(m, kernel_1d, mode="same"), axis=0, arr=array
    )
    smooth_y = np.apply_along_axis(
        lambda m: np.convolve(m, kernel_1d, mode="same"), axis=1, arr=array
    )
    avg = (smooth_x + smooth_y) / 2

    result = array * (1 - edge_mask * 0.6) + avg * edge_mask * 0.6
    result = np.clip(result, 0, 255).astype(np.uint8)

    return pg.surfarray.make_surface(result)


def mlaa_high(surf: pg.Surface, f4: bool = True) -> pg.Surface:
    """
    :param surf: pygame.Surface: Surface to apply high-quality MLAA to.
    :param f4: bool: If True, use float64 for calculations; otherwise, use float32.
    :return: pygame.Surface: A new surface with high-quality MLAA applied.
    """

    assert isinstance(surf, pg.Surface)
    assert isinstance(f4, bool)
    array = pg.surfarray.array3d(surface=surf).astype(
        np.float32 if not f4 else np.float64
    )
    gray = np.mean(array, axis=2)

    diff_x = np.abs(np.diff(gray, axis=0, append=gray[-1:]))
    diff_y = np.abs(np.diff(gray, axis=1, append=gray[:, -1:]))
    edge_mask = ((diff_x + diff_y) > 25).astype(
        np.float32 if not f4 else np.float64
    )[..., np.newaxis]

    kernel_1d = np.ones(7, dtype=(np.float32 if not f4 else np.float64)) / 7
    smooth_x = np.apply_along_axis(
        lambda m: np.convolve(m, kernel_1d, mode="same"), axis=0, arr=array
    )
    smooth_y = np.apply_along_axis(
        lambda m: np.convolve(m, kernel_1d, mode="same"), axis=1, arr=array
    )
    avg = (smooth_x + smooth_y) / 2

    result = array * (1 - edge_mask * 0.8) + avg * edge_mask * 0.8
    result = np.clip(result, 0, 255).astype(np.uint8)

    return pg.surfarray.make_surface(result)


def mlaa_very_high(surf: pg.Surface, f4: bool = True) -> pg.Surface:
    """
    :param surf: pygame.Surface: Surface to apply very high-quality MLAA to.
    :param f4: bool: If True, use float64 for calculations; otherwise, use float32.
    :return: pygame.Surface: A new surface with very high-quality MLAA applied.
    """
    assert isinstance(surf, pg.Surface)
    assert isinstance(f4, bool)
    array = pg.surfarray.array3d(surface=surf).astype(
        np.float32 if not f4 else np.float64
    )
    gray = np.mean(array, axis=2)

    diff_x = np.abs(np.diff(gray, axis=0, append=gray[-1:]))
    diff_y = np.abs(np.diff(gray, axis=1, append=gray[:, -1:]))
    edge_mask = ((diff_x + diff_y) > 16).astype(
        np.float32 if not f4 else np.float64
    )[..., np.newaxis]

    kernel_1d = np.ones(9, dtype=(np.float32 if not f4 else np.float64)) / 9
    smooth_x = np.apply_along_axis(
        lambda m: np.convolve(m, kernel_1d, mode="same"), axis=0, arr=array
    )
    smooth_y = np.apply_along_axis(
        lambda m: np.convolve(m, kernel_1d, mode="same"), axis=1, arr=array
    )
    avg = (smooth_x + smooth_y) / 2

    result = array * (1 - edge_mask * 0.9) + avg * edge_mask * 0.9
    result = np.clip(result, 0, 255).astype(np.uint8)

    return pg.surfarray.make_surface(result)


def mlaa(
    surf: pg.Surface,
    quality: Union[
        Literal["low", "medium", "high", "very_high", "default"], int
    ] = "default",
    f4: bool | None = None,
) -> pg.Surface:
    assert isinstance(surf, pg.Surface)
    assert quality in ["low", "medium", "high", "very_high", "default"] or (
        isinstance(quality, int) and (4 >= quality >= -1) and quality != 0
    )
    if isinstance(quality, str):
        quality = quality.lower()
        if quality == "low":
            return mlaa_low(surf, f4=f4 if f4 is not None else False)
        elif quality == "medium":
            return mlaa_medium(surf, f4=f4 if f4 is not None else False)
        elif quality == "high":
            return mlaa_high(surf, f4=f4 if f4 is not None else True)
        elif quality == "very_high":
            return mlaa_very_high(surf, f4=f4 if f4 is not None else True)
        elif quality == "default":
            return mlaa_medium(surf, f4=f4 if f4 is not None else False)
        else:
            raise ValueError(f"Unknown quality: {quality}")
    elif isinstance(quality, int):
        if quality == -1 or quality == 2:
            return mlaa_medium(surf, f4=f4 if f4 is not None else False)
        elif quality == 1:
            return mlaa_low(surf, f4=f4 if f4 is not None else False)
        elif quality == 3:
            return mlaa_high(surf, f4=f4 if f4 is not None else True)
        elif quality == 4:
            return mlaa_very_high(surf, f4=f4 if f4 is not None else True)
        elif quality == 0:
            if __debug__:
                print(
                    "MLAA with a quality of 0 (MLAA0x) doesn't exist, returning the original surface."
                )
            return surf
        else:
            raise ValueError(f"Unknown quality: {quality}")
    return surf


def mlaa_custom(
    surf: pg.Surface, threshold: int, kernel: int, blend: float, f4: bool
) -> pg.Surface:
    """
    Custom Morphological Anti-Aliasing function for Pygame-CE surfaces.
    :param surf: pygame.Surface: The surface to apply custom MLAA to.
    :param threshold: int: The threshold for edge detection (1-100).
    :param kernel: int: The size of the smoothing kernel (must be an odd integer > 1).
    :param blend: float: The blending factor (0.0 to 1.0).
    :param f4: bool: If True, use float64 for calculations; otherwise, use float32.
    :return: pygame.Surface: A new surface with custom MLAA applied.
    """
    assert isinstance(surf, pg.Surface)
    assert isinstance(threshold, int) and threshold > 0
    assert threshold <= 100
    assert isinstance(kernel, int) and kernel > 1
    assert kernel % 2 == 1, "Kernel size must be an odd integer."
    assert isinstance(blend, float) and 0 <= blend <= 1
    assert isinstance(f4, bool)

    array = pg.surfarray.array3d(surface=surf).astype(
        np.float32 if not f4 else np.float64
    )
    gray = np.mean(array, axis=2)

    diff_x = np.abs(np.diff(gray, axis=0, append=gray[-1:]))
    diff_y = np.abs(np.diff(gray, axis=1, append=gray[:, -1:]))
    edge_mask = ((diff_x + diff_y) > threshold).astype(
        np.float32 if not f4 else np.float64
    )[..., np.newaxis]

    kernel_1d = (
        np.ones(kernel, dtype=(np.float32 if not f4 else np.float64)) / kernel
    )
    smooth_x = np.apply_along_axis(
        lambda m: np.convolve(m, kernel_1d, mode="same"), axis=0, arr=array
    )
    smooth_y = np.apply_along_axis(
        lambda m: np.convolve(m, kernel_1d, mode="same"), axis=1, arr=array
    )
    avg = (smooth_x + smooth_y) / 2

    result = array * (1 - edge_mask * blend) + avg * edge_mask * blend
    result = np.clip(result, 0, 255).astype(np.uint8)

    return pg.surfarray.make_surface(result)


# Aliases for the MLAA functions
mlaa_lq = mlaa_low_quality = mlaa_low
mlaa_default = mlaa_med = mlaa_medium_quality = mlaa_mq = mlaa_medium
mlaa_hq = mlaa_high_quality = mlaa_high
mlaa_very_hq = mlaa_veryhigh = mlaa_vhq = mlaa_very_high_quality = (
    mlaa_veryhighquality
) = mlaa_very_high
custom_mlaa = mlaa_custom_quality = custom_mlaa_quality = mlaa_custom
