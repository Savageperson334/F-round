# polygon_area
#
# Copied verbatim from https://github.com/EMob-Lab/MnMS
#   file src/mnms/tools/geometry.py, line 58
#   licence (as GitHub reports it): LGPL-3.0   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def polygon_area(polygon):
    """Method that computes the area of a polygon based on Schoelace formula.

    Args:
        -polygon: defined by a list of points
    """
    x = [p[0] for p in polygon]
    y = [p[1] for p in polygon]
    area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
    return area
