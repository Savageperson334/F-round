# to_proper_degrees
#
# Copied verbatim from https://github.com/ericmjl/nxviz
#   file nxviz/polcart.py, line 43
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def to_proper_degrees(theta):
    """
    Converts theta (degrees) to be within -180 and 180.
    """
    if theta > 180 or theta < -180:
        theta = theta % 180
    return theta
