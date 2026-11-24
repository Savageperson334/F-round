# n_param_ZHAireS
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/atmosphere/refractivity.py, line 21
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def n_param_ZHAireS(h):
    """
    Parametrisation for the refractivity N = n - 1, as funtion of height above sea level N(h) as used in ZHAireS.

    Parameters
    ----------
    h : float
        Height over sea level in meter

    Returns
    -------

    refractivity : float
        Refractive index for given height
    """

    a = 325e-6
    b = 0.1218e-3
    return 1 + a * np.exp(-b * h)
