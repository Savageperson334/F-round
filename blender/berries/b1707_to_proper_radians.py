# to_proper_radians
#
# Copied verbatim from https://github.com/ericmjl/nxviz
#   file nxviz/polcart.py, line 34
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from numpy import pi


def to_proper_radians(theta):
    """
    Converts theta (radians) to be within -pi and +pi.
    """
    if theta > pi or theta < -pi:
        theta = theta % pi
    return theta
