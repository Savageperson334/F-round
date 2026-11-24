# make_periodic_seam
#
# Copied verbatim from https://github.com/xandergos/terrain-diffusion
#   file terrain_diffusion/inference/utils/azgaar_to_tiff.py, line 313
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def make_periodic_seam(array: np.ndarray, blend: int = 2) -> np.ndarray:
    """Reconcile opposite edges so modular tiling does not show a hard seam.

    Opposite borders are forced equal (required for seamless wrap). Interior
    pixels near the border are eased toward that shared average.
    """
    result = np.asarray(array, dtype=np.float32).copy()
    height, width = result.shape
    blend_x = max(1, min(blend, max(1, width // 4)))
    blend_y = max(1, min(blend, max(1, height // 4)))

    for offset in range(blend_x):
        # alpha=1 at the outer edge, fading to 0 toward the interior.
        alpha = 1.0 - (offset / blend_x)
        left = result[:, offset].copy()
        right = result[:, width - 1 - offset].copy()
        average = 0.5 * (left + right)
        result[:, offset] = (1.0 - alpha) * left + alpha * average
        result[:, width - 1 - offset] = (1.0 - alpha) * right + alpha * average

    for offset in range(blend_y):
        alpha = 1.0 - (offset / blend_y)
        top = result[offset, :].copy()
        bottom = result[height - 1 - offset, :].copy()
        average = 0.5 * (top + bottom)
        result[offset, :] = (1.0 - alpha) * top + alpha * average
        result[height - 1 - offset, :] = (1.0 - alpha) * bottom + alpha * average

    # Exact equality on the wrapped borders (and corners).
    result[:, 0] = result[:, -1] = 0.5 * (result[:, 0] + result[:, -1])
    result[0, :] = result[-1, :] = 0.5 * (result[0, :] + result[-1, :])
    corner = 0.25 * (
        result[0, 0] + result[0, -1] + result[-1, 0] + result[-1, -1]
    )
    result[0, 0] = result[0, -1] = result[-1, 0] = result[-1, -1] = corner
    return result
