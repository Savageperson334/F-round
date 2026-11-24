# smooth_river_bumps
#
# Copied verbatim from https://github.com/xandergos/terrain-diffusion
#   file terrain_diffusion/inference/postprocessing.py, line 87
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def smooth_river_bumps(
    height,
    slope_thresh=50,     # below this, considered "flat"
    smooth_strength=0.3,    # fraction of smoothing applied
    iterations=3            # few iterations are enough
):
    """
    Removes small upslope bumps in rivers while preserving steep slopes.
    """
    h = height.copy().astype(np.float32)
    nan_mask = np.isnan(h)

    for _ in range(iterations):
        # Compute gradients on a NaN-filled-safe surface (treat NaNs as 0 for ops)
        h_safe = np.where(nan_mask, 0.0, h)
        grad_y, grad_x = np.gradient(h_safe)
        slope = np.sqrt(grad_x**2 + grad_y**2)

        # Build Laplacian ignoring NaN neighbors (4-neighbor)
        valid = ~nan_mask
        up_valid = np.roll(valid, 1, 0)
        dn_valid = np.roll(valid, -1, 0)
        lf_valid = np.roll(valid, 1, 1)
        rt_valid = np.roll(valid, -1, 1)

        up = np.where(up_valid, np.roll(h_safe, 1, 0), 0.0)
        dn = np.where(dn_valid, np.roll(h_safe, -1, 0), 0.0)
        lf = np.where(lf_valid, np.roll(h_safe, 1, 1), 0.0)
        rt = np.where(rt_valid, np.roll(h_safe, -1, 1), 0.0)

        neighbor_sum = up + dn + lf + rt
        neighbor_cnt = (
            up_valid.astype(np.float32)
            + dn_valid.astype(np.float32)
            + lf_valid.astype(np.float32)
            + rt_valid.astype(np.float32)
        )
        laplace = neighbor_sum - neighbor_cnt * h_safe
        laplace[nan_mask] = 0.0

        # Weight by (low slope) regions only; do not update NaN cells
        w = np.exp(- (slope / slope_thresh) ** 2)
        w[nan_mask] = 0.0

        # Apply selective smoothing, preserve NaNs
        h += smooth_strength * w * laplace
        h[nan_mask] = np.nan

    return h
