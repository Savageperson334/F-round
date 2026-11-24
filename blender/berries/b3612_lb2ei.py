# lb2ei
#
# Copied verbatim from https://github.com/spacetelescope/jwst_coronagraph_visibility
#   file jwst_coronagraph_visibility/skyvec2ins.py, line 107
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def _wrap_to_2pi(scalar_or_arr):
    """Offsets angles outside 0 <= x <= 2 * pi to lie within the interval

    Parameters
    ----------
    scalar_or_arr : int or array
        Angle or array of angles, in radians.

    Returns
    -------
        Array of wrapped angles with values in the range [0, 2*pi].
    """
    return np.asarray(scalar_or_arr) % (2 * np.pi)


def lb2ei(lmlsun, beta):
    """Convert ecliptic coordinates (lambda-lambda_sun, beta) to alternative ecliptic coordinates (epsilon, i)
    according to Eq 11 in Leinert et al. 1998.

    Parameters
    ----------
    beta : numpy.ndarray
        Ecplitic longitude in radians.
    lmlsun : numpy.ndarray
        Ecliptic lattitude in radians.

    Returns
    -------
    elong : numpy.ndarray
        Elongation (angular distance from the sun to the field-of-view) in radians.
    inc : numpy.ndarray
        Inclination (position angle counted from the ecliptic counterclockwise) in radians.
    """
    # convert to an elongation in radians
    elong = np.arccos(np.cos(lmlsun) * np.cos(beta))
    cosinc = np.cos(beta) * np.sin(lmlsun) / np.sin(elong)
    sininc = np.sin(beta) / np.sin(elong)
    inc = np.arctan2(sininc, cosinc)  # make sure we get the right quadrant
    inc = _wrap_to_2pi(inc)
    # make inc lie between 0 - 2*pi
    # j = np.where(inc < 0.)
    # if len(j[0]) != 0:
    #     inc[j] += 2*np.pi
    # j = np.where(inc > 2*np.pi)
    # if len(j[0]) != 0:
    #     inc[j] -= 2*np.pi
    return elong, inc
