# get_offset
#
# Copied verbatim from https://github.com/POPCORNBOOM/EZHolodotNet
#   file Core/main.py, line 63
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np

offset_cache = {}


def get_offset(depth, t, a, b):
    if (depth, t, a, b) in offset_cache:
        return offset_cache[(depth, t, a, b)]
    offsetFactor = (1 + 3 * a) / 4
    c = depth / b
    offset = offsetFactor * c
    x0 = -c
    x1 = c
    y0 = -c + offset
    h_x0 = -c * a
    h_x1 = c * a
    h_y = -c * a + offset

    x = (
        np.power(1 - t, 3) * x0
        + 3 * np.power(1 - t, 2) * t * h_x0
        + 3 * (1 - t) * np.power(t, 2) * h_x1
        + np.power(t, 3) * x1
    )
    y = (
        np.power(1 - t, 3) * y0
        + 3 * np.power(1 - t, 2) * t * h_y
        + 3 * (1 - t) * np.power(t, 2) * h_y
        + np.power(t, 3) * y0
    )
    offset_cache[(depth, t, a, b)] = [x, y]
    return [x, y]
