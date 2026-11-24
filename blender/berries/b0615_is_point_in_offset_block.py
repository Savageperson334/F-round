# is_point_in_offset_block
#
# Copied verbatim from https://github.com/POPCORNBOOM/EZHolodotNet
#   file Core/main.py, line 166
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def is_point_in_offset_block(point, block, offset):
    if point[0] < min(block[0], block[0] + offset[0]):
        return False
    if point[0] > max(block[0] + 1, block[0] + offset[0] + 1):
        return False
    if point[1] < min(block[1], block[1] + offset[1]):
        return False
    if point[1] > max(block[1] + 1, block[1] + offset[1] + 1):
        return False

    if offset[0] == 0 or offset[1] == 0:
        return True

    k = offset[1] / offset[0]

    if k > 0:
        k1 = -np.sqrt(2) / 2
    else:
        k1 = np.sqrt(2) / 2

    x0 = point[0] - block[0] - 0.5
    y0 = point[1] - block[1] - 0.5

    x1 = (y0 - k1 * x0) / (k - k1)

    return abs(x1 - x0) <= 0.5
