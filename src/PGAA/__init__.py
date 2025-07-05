# encoding: utf-8
"""Anti-Aliasing for Pygame-CE surfaces."""

__version__ = "3.0.1"

import pygame as pg

assert pg.get_init(), (
    "Pygame must be initialized before using this module. "
    "Please call `pg.init()` before importing PGAA."
)
