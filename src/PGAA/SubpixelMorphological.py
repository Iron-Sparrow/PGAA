# encoding: utf-8

"""SMAA"""

from typing import Union, Literal

import numpy as np
import pygame as pg

from ._common import compute_luma


def smaa(
    surf: pg.Surface,
    threshold: Union[float, int] = 0.1,
    max_dist: int = 16,
    lut_size: int = 32,
    luma: Literal["rec709", "rec601", "rec2100", "mean"] = "rec709",
    f4: bool = False,
) -> pg.Surface:
    """
    :param luma:
    :param surf:
    :param threshold:
    :param max_dist:
    :param lut_size:
    :param f4:
    :return:
    """

    assert isinstance(surf, pg.Surface)
    assert isinstance(threshold, (int, float))
    assert isinstance(max_dist, int) and max_dist > 0
    assert isinstance(lut_size, int) and lut_size > 0
    assert isinstance(f4, bool)

    array = (
        pg.surfarray.array3d(surf).astype(
            np.float32 if not f4 else np.float64
        )
        / 255.0
    )
    h, w = array.shape[:2]

    luminance = compute_luma(array, luma)

    grad_h = np.abs(np.roll(luminance, -1, 0) - luminance) > threshold
    grad_v = np.abs(np.roll(luminance, -1, 1) - luminance) > threshold

    color_h = np.any(
        np.abs(np.roll(array, -1, 0) - array) > threshold, axis=2
    )
    color_v = np.any(
        np.abs(np.roll(array, -1, 1) - array) > threshold, axis=2
    )

    mask_h = (grad_h | color_h).astype(np.float32 if not f4 else np.float64)
    mask_v = (grad_v | color_v).astype(np.float32 if not f4 else np.float64)

    # Distance transforms for H, V, D1, D2
    def compute_dist(mask):
        dist = np.full(shape=(h, w), fill_value=max_dist, dtype=np.uint16)
        dist[mask.astype(bool)] = 0
        for i in range(1, max_dist):
            dist = np.minimum(dist, np.roll(dist, +1, axis=0) + 1)
            dist = np.minimum(dist, np.roll(dist, -1, axis=0) + 1)
            dist = np.minimum(dist, np.roll(dist, +1, axis=1) + 1)
            dist = np.minimum(dist, np.roll(dist, -1, axis=1) + 1)
        return dist.astype(np.float32 if not f4 else np.float64) / max_dist

    dist_h = compute_dist(mask_h)
    dist_v = compute_dist(mask_v)
    dist_d1 = compute_dist((mask_h & mask_v))
    dist_d2 = dist_d1.copy()

    # LUT creation (H,V,D1,D2 weights)
    xs = np.linspace(0, 1, lut_size)
    grad_vals = xs[:, None]
    dist_vals = xs[None, :]
    base = np.exp(-((dist_vals * 2 - 1) ** 2) / 0.08) * grad_vals
    lut = np.stack([base, base, base, base], axis=-1)

    # Shape/corner suppression
    corner = (mask_h.astype(bool) & mask_v.astype(bool)).astype(
        np.float32 if not f4 else np.float64
    )
    combined_mask = np.clip(mask_h + mask_v, 0, 1) * (1 - corner)

    # Weighted multi-direction blend
    idx_h = (dist_h * (lut_size - 1)).astype(np.int32)
    idx_v = (dist_v * (lut_size - 1)).astype(np.int32)
    idx_d1 = (dist_d1 * (lut_size - 1)).astype(np.int32)
    idx_d2 = (dist_d2 * (lut_size - 1)).astype(np.int32)

    w_h = lut[idx_h, idx_h, 0] * combined_mask
    w_v = lut[idx_v, idx_v, 1] * combined_mask
    w_d1 = lut[idx_d1, idx_d1, 2] * combined_mask
    w_d2 = lut[idx_d2, idx_d2, 3] * combined_mask

    # Neighbour fetch
    n_h = np.roll(array, -1, 0)
    n_v = np.roll(array, -1, 1)
    n_d1 = np.roll(np.roll(array, -1, 0), -1, 1)
    n_d2 = np.roll(np.roll(array, -1, 0), +1, 1)

    total_w = w_h + w_v + w_d1 + w_d2
    blended = (
        array * (1 - total_w[..., None])
        + n_h * w_h[..., None]
        + n_v * w_v[..., None]
        + n_d1 * w_d1[..., None]
        + n_d2 * w_d2[..., None]
    )

    result = np.clip(blended * 255, 0, 255).astype(np.uint8)
    return pg.surfarray.make_surface(result)


def smaa_low(surf: pg.Surface, f4: bool = False) -> pg.Surface:
    """
    :param surf: pygame.Surface:
    :param f4: bool:
    :return: pygame.Surface:
    """
    return smaa(surf, 0.2, 4, 16, "rec709", f4)


def smaa_medium(surf: pg.Surface, f4: bool = False) -> pg.Surface:
    """
    :param surf: pygame.Surface:
    :param f4: bool:
    :return: pygame.Surface:
    """
    return smaa(surf, 0.1, 8, 32, "rec709", f4)


def smaa_high(surf: pg.Surface, f4: bool = True) -> pg.Surface:
    """
    :param surf: pygame.Surface:
    :param f4: bool:
    :return: pygame.Surface:
    """
    return smaa(surf, 0.05, 16, 48, "rec709", f4)


def smaa_very_high(surf: pg.Surface, f4: bool = True) -> pg.Surface:
    """
    :param surf: pygame.Surface:
    :param f4: bool:
    :return: pygame.Surface:
    """
    return smaa(surf, 0.03, 24, 64, "rec709", f4)


def smaa_ultra(surf: pg.Surface, f4: bool = True) -> pg.Surface:
    """
    :param surf: pygame.Surface:
    :param f4: bool:
    :return: pygame.Surface:
    """
    return smaa(surf, 0.0125, 32, 256, "rec709", f4)


# Aliases
smaa_lq = smaa28_low = smaa28_lq = smaa_low_quality = smaa28_low_quality = (
    smaa_low
)
smaa_default = smaa28_default = smaa_mq = smaa28_medium = smaa28_mq = (
    smaa_medium_quality
) = smaa28_medium_quality = smaa_medium
smaa_hq = smaa28_high = smaa28_hq = smaa_high_quality = (
    smaa28_high_quality
) = smaa_high
smaa_vhq = smaa28_very_high = smaa28_vhq = smaa_very_high_quality = (
    smaa28_very_high_quality
) = smaa28_very_hq = smaa_very_hq = smaa_very_high
smaa_uhq = smaa28_ultra = smaa_ultra_high_quality = (
    smaa28_ultra_high_quality
) = smaa28_uhq = smaa_ultra_quality = smaa28_ultra_quality = (
    smaa28_ultra_hq
) = smaa_ultra_hq = smaa_ultra
