# angle_difference
#
# Copied verbatim from https://github.com/cbassa/stvid
#   file stvid/fourframe.py, line 1057
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def angle_difference(ang1, ang2):
    x1, y1 = np.cos(ang1), np.sin(ang1)
    x2, y2 = np.cos(ang2), np.sin(ang2)

    return np.arccos(x1 * x2 + y1 * y2)
