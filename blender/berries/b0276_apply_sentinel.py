# apply_sentinel
#
# Copied verbatim from https://github.com/GalaxyUrsa/Pisces-Explorer
#   file backend/plotting/common.py, line 58
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Ocean currents and fluid dynamics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def apply_sentinel(data, sentinel: float, vmin: float, vmax: float):
    """Replace NaN with a sentinel and clamp valid values to the color range."""
    output = np.array(data, dtype=float)
    valid = ~np.isnan(output)
    output[valid] = np.clip(output[valid], vmin, vmax)
    output[~valid] = sentinel
    return output
