import numpy as np
import pygame


def _smaa28(
    surface: pygame.Surface,
    threshold: float = 0.1,
    max_dist: int = 16,
    lut_size: int = 32,
) -> pygame.Surface:
    arr = pygame.surfarray.array3d(surface).astype(np.float32) / 255.0
    h, w, _ = arr.shape

    # 1. Luma + Color edge detection
    luma = arr[..., 0] * 0.2126 + arr[..., 1] * 0.7152 + arr[..., 2] * 0.0722
    grad_h = np.abs(np.roll(luma, -1, 0) - luma) > threshold
    grad_v = np.abs(np.roll(luma, -1, 1) - luma) > threshold

    color_h = np.any(np.abs(np.roll(arr, -1, 0) - arr) > threshold, axis=2)
    color_v = np.any(np.abs(np.roll(arr, -1, 1) - arr) > threshold, axis=2)

    mask_h = (grad_h | color_h).astype(np.float32)
    mask_v = (grad_v | color_v).astype(np.float32)

    # 2. Distance transforms for H, V, D1, D2
    def compute_dist(mask):
        dist = np.full((h, w), max_dist, dtype=np.int32)
        dist[mask.astype(bool)] = 0
        for i in range(1, max_dist):
            dist = np.minimum(dist, np.roll(dist, +1, axis=0) + 1)
            dist = np.minimum(dist, np.roll(dist, -1, axis=0) + 1)
            dist = np.minimum(dist, np.roll(dist, +1, axis=1) + 1)
            dist = np.minimum(dist, np.roll(dist, -1, axis=1) + 1)
        return dist.astype(np.float32) / max_dist

    dist_h = compute_dist(mask_h)
    dist_v = compute_dist(mask_v)
    dist_d1 = compute_dist((mask_h & mask_v))
    dist_d2 = dist_d1.copy()

    # 3. LUT creation (H,V,D1,D2 weights)
    xs = np.linspace(0, 1, lut_size)
    grad_vals = xs[:, None]
    dist_vals = xs[None, :]
    base = np.exp(-((dist_vals * 2 - 1) ** 2) / 0.08) * grad_vals
    lut = np.stack([base, base, base, base], axis=-1)

    # 4. Shape/corner suppression
    corner = (mask_h.astype(bool) & mask_v.astype(bool)).astype(np.float32)
    combined_mask = np.clip(mask_h + mask_v, 0, 1) * (1 - corner)

    # 5. Weighted multi-direction blend
    idx_h = (dist_h * (lut_size - 1)).astype(np.int32)
    idx_v = (dist_v * (lut_size - 1)).astype(np.int32)
    idx_d1 = (dist_d1 * (lut_size - 1)).astype(np.int32)
    idx_d2 = (dist_d2 * (lut_size - 1)).astype(np.int32)

    w_h = lut[idx_h, idx_h, 0] * combined_mask
    w_v = lut[idx_v, idx_v, 1] * combined_mask
    w_d1 = lut[idx_d1, idx_d1, 2] * combined_mask
    w_d2 = lut[idx_d2, idx_d2, 3] * combined_mask

    # Neighbor fetch
    n_h = np.roll(arr, -1, 0)
    n_v = np.roll(arr, -1, 1)
    n_d1 = np.roll(np.roll(arr, -1, 0), -1, 1)
    n_d2 = np.roll(np.roll(arr, -1, 0), +1, 1)

    total_w = w_h + w_v + w_d1 + w_d2
    blended = (
        arr * (1 - total_w[..., None])
        + n_h * w_h[..., None]
        + n_v * w_v[..., None]
        + n_d1 * w_d1[..., None]
        + n_d2 * w_d2[..., None]
    )

    result = np.clip(blended * 255, 0, 255).astype(np.uint8)
    return pygame.surfarray.make_surface(result)
