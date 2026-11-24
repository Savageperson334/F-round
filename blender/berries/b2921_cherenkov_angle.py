# cherenkov_angle
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/atmosphere/cherenkov_radius.py, line 131
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def cherenkov_angle(n):
    """ Return cherenkov angle for given refractive index.

    Paramter:

    n : double
        Refractive index

    Return : cherenkov angle

    """
    return np.arccos(1 / n)
