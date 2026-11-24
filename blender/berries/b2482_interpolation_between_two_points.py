# interpolation_between_two_points
#
# Copied verbatim from https://github.com/jlanversin/ONIX
#   file onix/utils/functions.py, line 959
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def interpolation_between_two_points(pair1, pair2, x):
    """Linearly interpolates between two points to find the ordinate to a given abscissa value (x).

    Parameters
    ----------
    pair1: List of two floats
    pair2: List of two floats
    x: float
        Abscissa of the point for which the ordinate is calculated
    """
    a = (pair2[1] - pair1[1])/(pair2[0] - pair1[0])
    b = (pair1[1]*pair2[0] - pair1[0]*pair2[1])/(pair2[0] - pair1[0])

    y = a*x+b

    return y
