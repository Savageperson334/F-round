# encode
#
# Copied verbatim from https://github.com/Flowm/satvis
#   file scripts/starmap/cubemap.py, line 208
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def encode(linear: np.ndarray, exposure: float) -> np.ndarray:
    """Linear radiance to 8-bit sRGB, through Reinhard so bright stars stay distinct."""
    x = np.maximum(linear * exposure, 0.0)
    tone = x / (1.0 + x)
    srgb = np.power(tone, 1.0 / 2.2)
    return np.clip(srgb * 255.0 + 0.5, 0, 255).astype(np.uint8)
