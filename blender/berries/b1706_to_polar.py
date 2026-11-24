# to_polar
#
# Copied verbatim from https://github.com/ericmjl/nxviz
#   file nxviz/polcart.py, line 21
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from numpy import arctan2 as atan2
import numpy as np
from numpy import sqrt


def to_polar(x, y):
    """
    Converts cartesian x, y to polar r, theta.
    """
    theta = atan2(y, x)
    r = sqrt(x**2 + y**2)

    if theta < 0:
        theta += 2 * np.pi

    return r, theta
