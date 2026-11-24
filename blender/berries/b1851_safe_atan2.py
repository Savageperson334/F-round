# safe_atan2
#
# Copied verbatim from https://github.com/fatiando/fatiando
#   file fatiando/gravmag/_prism_numpy.py, line 14
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from numpy import arctan2
from numpy import pi


def safe_atan2(y, x):
    """
    Correct the value of the angle returned by arctan2 to match the sign of the
    tangent. Also return 0 instead of 2Pi for 0 tangent.
    """
    res = arctan2(y, x)
    res[y == 0] = 0
    res[(y > 0) & (x < 0)] -= pi
    res[(y < 0) & (x < 0)] += pi
    return res
