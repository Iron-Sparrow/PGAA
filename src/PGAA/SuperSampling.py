"""
Functions for applying various forms of Super Sampling Anti-Aliasing (SSAA) to surfaces.
Due to the nature of SSAA, it is expected that the performances will be lower than without any form of anti-aliasing.

Note: This class is designed to work with Pygame-CE (Pygame Community Edition) and isn't compatible with other versions of Pygame.
It requires Pygame-CE 2.2.1 or later for it to function correctly. It only works on ARM64 architectures from Pygame-CE 2.4.0 onwards.

Currently SSAA0.5x, SSAA2x, and SSAA4x, SSAA8x, SSAA32x are implemented and customisable versions are possible through the `ssaa` function.
"""

import pygame as pg
from typing import Union

assert getattr(pg, "IS_CE", False), (
    "This module is designed to work with Pygame-CE (Pygame Community Edition) only."
)


def ssaa05(surf: pg.Surface) -> pg.Surface:
    """
    Applies SSAA 0.5x to the given surface and returns a new surface of the same size.
    Uses the default scaling algorithm for better performance.
    :param surf :pygame.Surface: The surface to apply SSAA to.
    :return: pygame.Surface: A new surface with SSAA applied.
    """
    assert isinstance(surf, pg.Surface)
    assert surf.get_width() % 2 == 0 and surf.get_height() % 2 == 0, (
        "Surface dimensions must be even for SSAA."
    )
    return pg.transform.scale2x(pg.transform.scale_by(surf, 0.5))


def ssaa05_hq(surf: pg.Surface) -> pg.Surface:
    """
    Applies SSAA 0.5x to the given surface and returns a new surface of the same size.
    Uses the smoothed scaling algorithm for better quality.
    :param surf :pygame.Surface: The surface to apply SSAA to.
    :return: pygame.Surface: A new surface with SSAA applied.
    """
    assert isinstance(surf, pg.Surface)
    assert surf.get_width() % 2 == 0 and surf.get_height() % 2 == 0, (
        "Surface dimensions must be even for SSAA."
    )
    return pg.transform.scale2x(pg.transform.smoothscale_by(surf, 0.5))


def ssaa05_lq(surf: pg.Surface) -> pg.Surface:
    assert isinstance(surf, pg.Surface)
    assert surf.get_width() % 2 == 0 and surf.get_height() % 2 == 0, (
        "Surface dimensions must be even for SSAA."
    )
    return pg.transform.scale_by(pg.transform.scale_by(surf, 0.5), 2)


def ssaa2(surf: pg.Surface) -> pg.Surface:
    """
    Apples SSAA 2x to the give surface and returns a new surface of the same size.
    Uses the default scaling algorithm for better performance.
    :param surf :pygame.Surface: The surface to apply SSAA to.
    :return: pygame.Surface: A new surface with SSAA applied.
    """
    assert isinstance(surf, pg.Surface)
    return pg.transform.scale_by(pg.transform.scale2x(surf), 0.5)


def ssaa2_hq(surf: pg.Surface) -> pg.Surface:
    """
    Applies SSAA 2x to the given surface and returns a new surface of the same size.
    Uses the smoothed scaling algorithm for better quality.
    :param surf :pygame.Surface: The surface to apply SSAA to.
    :return: pygame.Surface: A new surface with SSAA applied.
    """
    assert isinstance(surf, pg.Surface)
    return pg.transform.smoothscale_by(pg.transform.scale2x(surf), 0.5)


def ssaa2_lq(surf: pg.Surface) -> pg.Surface:
    assert isinstance(surf, pg.Surface)
    return pg.transform.scale_by(pg.transform.scale_by(surf, 2), 0.5)


def ssaa4(surf: pg.Surface) -> pg.Surface:
    """
    Applies SSAA 4x to the given surface and returns a new surface of the same size.
    Uses the default scaling algorithm for better performance.
    :param surf :pygame.Surface: The surface to apply SSAA to.
    :return: pygame.Surface: A new surface with SSAA applied.
    """
    assert isinstance(surf, pg.Surface)
    return pg.transform.scale_by(pg.transform.scale_by(surf, 4), 0.25)


def ssaa4_hq(surf: pg.Surface) -> pg.Surface:
    """
    Applies SSAA 4x to the given surface and returns a new surface of the same size.
    Uses the smoothed scaling algorithm for better quality.
    :param surf :pygame.Surface: The surface to apply SSAA to.
    :return: pygame.Surface: A new surface with SSAA applied.
    """
    assert isinstance(surf, pg.Surface)
    return pg.transform.smoothscale_by(
        pg.transform.smoothscale_by(surf, 4), 0.25
    )


def ssaa8(surf: pg.Surface) -> pg.Surface:
    """
    Applies SSAA 8x to the given surface and returns a new surface of the same size.
    Uses the default scaling algorithm for better performance.

    It is not recommended to use this function due to the performance impact.

    :param surf :pygame.Surface: The surface to apply SSAA to.
    :return: pygame.Surface: A new surface with SSAA applied.
    """
    assert isinstance(surf, pg.Surface)
    assert pg.version.vernum.major >= 2 and pg.version.vernum.minor >= 4, (
        "SSAA8x requires Pygame-CE 2.4.0 or later. The hardware acceleration is required."
    )
    return pg.transform.scale_by(pg.transform.scale_by(surf, 8), 0.125)


def ssaa8_hq(surf: pg.Surface) -> pg.Surface:
    """
    Applies SSAA 8x to the given surface and returns a new surface of the same size.
    Uses the smoothed scaling algorithm for better quality.

    It is not recommended to use this function due to the performance impact.

    :param surf :pygame.Surface: The surface to apply SSAA to.
    :return: pygame.Surface: A new surface with SSAA applied.
    """
    assert isinstance(surf, pg.Surface)
    assert pg.version.vernum.major >= 2 and pg.version.vernum.minor >= 4, (
        "SSAA8x requires Pygame-CE 2.4.0 or later. The hardware acceleration is required."
    )
    return pg.transform.smoothscale_by(
        pg.transform.smoothscale_by(surf, 8), 0.125
    )


def ssaa32(surf: pg.Surface) -> pg.Surface:
    assert isinstance(surf, pg.Surface)
    if __debug__:
        print(
            "SSAA32x is for benchmarking purposes only, it is not to be used in any code not involving benchmarking."
        )
    assert pg.version.vernum.major >= 2 and pg.version.vernum.minor >= 4, (
        "SSAA32x requires Pygame-CE 2.4.0 or later. The hardware acceleration is required."
    )
    return pg.transform.smoothscale_by(
        pg.transform.smoothscale_by(surf, 32), (1 / 32)
    )


def ssaa(
    surf: pg.Surface, factor: Union[float, int] = 2, hq: bool = True
) -> pg.Surface:
    """
    Applies Super Sampling Anti-Aliasing (SSAA) to the given surface based on the specified factor.

    This function allows custom levels of SSAA, and works as a wrapper for multiple SSAA functions:

    - SSAA 0.5x: `ssaa05` or `ssaa05_hq`
    - SSAA 2x: `ssaa2` or `ssaa2_hq`
    - SSAA 4x: `ssaa4` or `ssaa4_hq`
    - SSAA 8x: `ssaa8` or `ssaa8_hq`
    - SSAA 32x: `ssaa32`

    It is actually slower to use this function than to use the specific SSAA functions directly, but it provides a convenient way to apply SSAA based on a factor that isn't hard-coded.

    :param surf: pygame.Surface: The surface to apply SSAA to.
    :param factor: Union[0.5, (unsigned) int]: The SSAA factor to apply.
    :param hq: bool: If True, uses high-quality scaling (smooth scaling), otherwise uses the default scaling.
    :return: pygame.Surface: A new surface with SSAA applied.

    SSAA lq is on purpose not available in the `ssaa` function, as it is not recommended to use it, due to risk of performance issues with worse visuals.
    """

    assert isinstance(surf, pg.Surface)
    assert isinstance(factor, int) or factor == 0.5
    assert factor <= 256, (
        "SSAA factor must be less than or equal to 256, although it is not recommended to use anything above 4 let alone 32."
    )
    assert factor > 0, "SSAA factor must be greater than 0."

    if factor == 0.5:
        if hq:
            return ssaa05_hq(surf)
        return ssaa05(surf)
    elif factor == 2:
        if hq:
            return ssaa2_hq(surf)
        return ssaa2(surf)
    elif factor == 4:
        if hq:
            return ssaa4_hq(surf)
        return ssaa4(surf)
    elif factor == 8:
        if hq:
            return ssaa8_hq(surf)
        return ssaa8(surf)
    elif factor == 32:
        return ssaa32(surf)
    elif factor == 1:
        if __debug__:
            print(
                "SSAA with a factor of 1 (SSAA1x) doesn't exists, returning the original surface."
            )
        return surf
    else:
        if hq:
            return pg.transform.smoothscale_by(
                pg.transform.smoothscale_by(surf, factor), 1 / factor
            )
        return pg.transform.scale_by(
            pg.transform.scale_by(surf, factor), 1 / factor
        )

    # If somehow, the code doesn't return anything, we return the original surface.
    return surf


def ssaa_lq(surf: pg.Surface, factor: Union[float, int] = 2) -> pg.Surface:
    """
    Alias of the function `ssaa` with `hq=False`.

    :param surf: pygame.Surface: The surface to apply SSAA to.
    :param factor: Union[0.5, (unsigned) int]: The SSAA factor to apply.
    :return: pygame.Surface: A new surface with SSAA applied.
    """
    return ssaa(surf, factor, hq=False)


def ssaa_hq(surf: pg.Surface, factor: Union[float, int] = 2) -> pg.Surface:
    """
    Alias of the function `ssaa` with `hq=True`.

    :param surf: pygame.Surface: The surface to apply SSAA to.
    :param factor: Union[0.5, (unsigned) int]: The SSAA factor to apply.
    :return: pygame.Surface: A new surface with SSAA applied.
    """
    return ssaa(surf, factor, hq=True)


# Aliases for the SSAA functions
ssaa_05 = ssaa_05x = ssaa05x = ssaa05
ssaa_05_hq = ssaa_05x_hq = ssaa05x_hq = ssaa05_hq
ssaa_05_lq = ssaa_05x_lq = ssaa05x_lq = ssaa05_lq
ssaa_2 = ssaa_2x = ssaa2x = ssaa2
ssaa_2_hq = ssaa_2x_hq = ssaa2x_hq = ssaa_default = ssaa2_hq
ssaa_2_lq = ssaa_2x_lq = ssaa2x_lq = ssaa2_lq
ssaa_4 = ssaa_4x = ssaa4x = ssaa4
ssaa_4_hq = ssaa_4x_hq = ssaa4x_hq = ssaa4_hq
ssaa_8 = ssaa_8x = ssaa8x = ssaa8
ssaa_8_hq = ssaa_8x_hq = ssaa8x_hq = ssaa8_hq
ssaa_32 = ssaa_32x = ssaa32x = ssaa32_hq = ssaa_32_hq = ssaa32x_hq = (
    ssaa_32x_hq
) = ssaa32
ssaa_low = ssaa_low_quality = ssaa_lq
ssaa_high = ssaa_high_quality = ssaa_hq
