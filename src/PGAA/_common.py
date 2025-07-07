# encoding: utf-8
from typing import Literal

import numpy as np
import pygame as pg

assert getattr(pg, "IS_CE", False), (
    "This module is designed to work with Pygame-CE (Pygame Community Edition) only."
)

del pg


def compute_luma(
    array: np.ndarray,
    luma: Literal["rec709", "rec601", "rec2100", "mean"] = "mean",
) -> np.ndarray:
    """
    Compute luma based on the specified standard.

    :param array: numpy.ndarray:
    :param luma: str: ("rec709", "rec601", "rec2100", "mean")
    :return: numpy.ndarray
    """

    assert isinstance(luma, str) and luma in (
        "rec709",
        "rec601",
        "rec2100",
        "mean",
    )

    if luma == "rec709":
        return (
            array[..., 0] * 0.2126
            + array[..., 1] * 0.7152
            + array[..., 2] * 0.0722
        )
    elif luma == "rec601":
        return (
            array[..., 0] * 0.299
            + array[..., 1] * 0.587
            + array[..., 2] * 0.114
        )
    elif luma == "rec2100":
        return (
            array[..., 0] * 0.2627
            + array[..., 1] * 0.6780
            + array[..., 2] * 0.0593
        )
    else:  # mean
        return np.mean(array, axis=2)
