# to_cartesian
#
# Copied verbatim from https://github.com/ericmjl/nxviz
#   file nxviz/polcart.py, line 8
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from numpy import cos
from numpy import sin
from numpy import pi


def to_proper_radians(theta):
    """
    Converts theta (radians) to be within -pi and +pi.
    """
    if theta > pi or theta < -pi:
        theta = theta % pi
    return theta


def to_cartesian(r, theta, proper=False):
    """
    Converts polar r, theta to cartesian x, y.
    """

    if proper:
        theta = to_proper_radians(theta)
    x = r * cos(theta)
    y = r * sin(theta)

    return x, y
