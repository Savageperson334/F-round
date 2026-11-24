# to_radians
#
# Copied verbatim from https://github.com/ericmjl/nxviz
#   file nxviz/polcart.py, line 61
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from numpy import pi


def to_proper_degrees(theta):
    """
    Converts theta (degrees) to be within -180 and 180.
    """
    if theta > 180 or theta < -180:
        theta = theta % 180
    return theta


def to_radians(theta):
    """
    Converts theta in degrees to theta in radians.
    """
    theta = to_proper_degrees(theta)
    return theta * pi / 180
