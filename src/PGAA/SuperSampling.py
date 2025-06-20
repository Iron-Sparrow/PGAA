"""
Functions for applying various forms of Super Sampling Anti-Aliasing (SSAA) to surfaces.
Due to the nature of SSAA, it is expected that the performances will be lower than without any form of anti-aliasing.

Note: This class is designed to work with Pygame-CE (Pygame Community Edition) and isn't compatible with other versions of Pygame.
It requires Pygame-CE 2.2.1 or later for it to function correctly. It only works on ARM64 architectures from Pygame-CE 2.4.0 onwards.

Currently only SSAA0.5x, SSAA2x, and SSAA4x are implemented.
"""

import pygame as pg

assert getattr(pg, "IS_CE", False), (
    "This module is designed to work with Pygame-CE (Pygame Community Edition) only."
)


def aa05(surf: pg.Surface) -> pg.Surface:
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


def aa05_hq(surf: pg.Surface) -> pg.Surface:
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


def aa2(surf: pg.Surface) -> pg.Surface:
    """
    Apples SSAA 2x to the give surface and returns a new surface of the same size.
    Uses the default scaling algorithm for better performance.
    :param surf :pygame.Surface: The surface to apply SSAA to.
    :return: pygame.Surface: A new surface with SSAA applied.
    """
    assert isinstance(surf, pg.Surface)
    return pg.transform.scale_by(pg.transform.scale2x(surf), 0.5)


def aa2_hq(surf: pg.Surface) -> pg.Surface:
    """
    Applies SSAA 2x to the given surface and returns a new surface of the same size.
    Uses the smoothed scaling algorithm for better quality.
    :param surf :pygame.Surface: The surface to apply SSAA to.
    :return: pygame.Surface: A new surface with SSAA applied.
    """
    assert isinstance(surf, pg.Surface)
    return pg.transform.smoothscale_by(pg.transform.scale2x(surf), 0.5)


def aa4(surf: pg.Surface) -> pg.Surface:
    """
    Applies SSAA 4x to the given surface and returns a new surface of the same size.
    Uses the default scaling algorithm for better performance.
    :param surf :pygame.Surface: The surface to apply SSAA to.
    :return: pygame.Surface: A new surface with SSAA applied.
    """
    assert isinstance(surf, pg.Surface)
    return pg.transform.scale_by(pg.transform.scale_by(surf, 4), 0.25)


def aa4_hq(surf: pg.Surface) -> pg.Surface:
    """
    Applies SSAA 4x to the given surface and returns a new surface of the same size.
    Uses the smoothed scaling algorithm for better quality.
    :param surf :pygame.Surface: The surface to apply SSAA to.
    :return: pygame.Surface: A new surface with SSAA applied.
    """
    assert isinstance(surf, pg.Surface)
    return pg.transform.smoothscale_by(pg.transform.smoothscale_by(surf, 4), 0.25)

def aa8(surf: pg.Surface) -> pg.Surface:
    """
    Applies SSAA 8x to the given surface and returns a new surface of the same size.
    Uses the default scaling algorithm for better performance.

    It is not recommended to use this function due to the performance impact.

    :param surf :pygame.Surface: The surface to apply SSAA to.
    :return: pygame.Surface: A new surface with SSAA applied.
    """
    assert isinstance(surf, pg.Surface)
    return pg.transform.scale_by(pg.transform.scale_by(surf, 8), 0.125)

def aa8_hq(surf: pg.Surface) -> pg.Surface:
    """
    Applies SSAA 8x to the given surface and returns a new surface of the same size.
    Uses the smoothed scaling algorithm for better quality.

    It is not recommended to use this function due to the performance impact.

    :param surf :pygame.Surface: The surface to apply SSAA to.
    :return: pygame.Surface: A new surface with SSAA applied.
    """
    assert isinstance(surf, pg.Surface)
    return pg.transform.smoothscale_by(pg.transform.smoothscale_by(surf, 8), 0.125)
