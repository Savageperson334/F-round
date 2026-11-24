# get_intersection_between_circle_and_line
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/helper.py, line 132
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def get_intersection_between_circle_and_line(r, b, c):
    """
    solution from: https://cp-algorithms.com/geometry/circle-line-intersection.html
    calculation in 2 dimension.

    Parameters
    ------------
    r : float
        circle radius in meter
    b, c: float, float
        line parameter

    Returns
    --------
    x0, y0 : float, float
        coordinates of intersection(s)
    """
    a = 1  # without loss of generality set a to 1
    eps = 1.e-6
    r0 = (a ** 2 + b ** 2)
    x0 = -a * c / r0
    y0 = -b * c / r0
    if c ** 2 > r ** 2 * r0 + eps:
        # no intersection
        return 0, 0
    elif np.abs(c ** 2 - r ** 2 * r0) < eps:
        # one intersection
        return x0, y0
    else:
        # two intersections
        d = r ** 2 - c ** 2 / r0
        mult = np.sqrt(d / r0)
        return x0 + b * mult, y0 - a * mult, x0 - b * mult, y0 + a * mult
