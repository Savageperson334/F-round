# ei2lb
#
# Copied verbatim from https://github.com/spacetelescope/jwst_coronagraph_visibility
#   file jwst_coronagraph_visibility/skyvec2ins.py, line 141
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def ei2lb(elong, inc):
    """Convert alternative ecliptic coordinates (epsilon, i) to ecliptic coordinates (lambda-lambda_sun, beta)
    according to Eq 12 in Leinert et al. 1998.

    Parameters
    ----------
    elong : numpy.ndarray
        Elongation (angular distance from the sun) in radians.
    inc : numpy.ndarray
        Inclination (position angle counted from the ecliptic counterclockwise) in radians.

    Returns
    -------
    lmlsun : numpy.ndarray
        Differential helioecliptic longitude in radians.
    beta : numpy.ndarray
        Ecliptic latitude in radians.
    """
    beta = np.arcsin(np.sin(inc) * np.sin(elong))
    coslmlsun = np.cos(elong) / np.cos(beta)
    sinlmlsun = np.cos(inc) * np.sin(elong) / np.cos(beta)
    lmlsun = np.arctan2(sinlmlsun, coslmlsun)
    return lmlsun, beta
