# cherenkov_radius
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/atmosphere/cherenkov_radius.py, line 145
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def cherenkov_radius(angle, d):
    """ Return (cherenkov) radius

    Paramters
    ---------

    angle : double
        (Opening) angle of the cone (in rad)

    d : double
        Heigth of the cone (typically called distance, in meter)

    Returns
    -------

    radius : double
        (Cherenkov) radius

    """
    return np.tan(angle) * d
