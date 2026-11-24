# ad2lb
#
# Copied verbatim from https://github.com/spacetelescope/jwst_coronagraph_visibility
#   file jwst_coronagraph_visibility/skyvec2ins.py, line 77
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def _tenv(dd, mm, ss):
    """Convert angle from sexagesimal (DMS) to decimal degree notation.

    Parameters
    ----------
    ss : int
        Seconds of sexagesimal measure
    mm : int
        Minutes of sexagesimal measure
    dd : int
        Degrees of sexagesimal measure

    Returns
    -------
        Angle in decimal degrees.
    """
    sgn, dd_mag = dd / dd, np.abs(dd)
    return sgn * (dd_mag + np.abs(mm) / 60.0 + np.abs(ss) / 3600.0)


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


def ad2lb(alpha_rad, delta_rad):
    """Convert equatorial coordinates (RA, Dec, i.e. alpha, delta) to ecliptic coordinates (lambda, beta)
    according to Eq 3 in Leinert et al. 1998.

    Parameters
    ----------
    alpha_rad : numpy.ndarray
        Right ascension in radians.
    delta_rad : numpy.ndarray
        Declination in radians.

    Returns
    -------
    lambda_rad : numpy.ndarray
        Ecliptic longitude in radians.
    beta_rad : numpy.ndarray
        Ecliptic latitude in radians.
    """
    obliq = _tenv(23, 26, 21.45)  # J2000 obliquity of Earth in degrees
    obliq *= np.pi / 180.0

    beta_rad = np.arcsin(np.sin(delta_rad) * np.cos(obliq) - np.cos(delta_rad) * np.sin(obliq) * np.sin(alpha_rad))
    coslambda = np.cos(alpha_rad) * np.cos(delta_rad) / np.cos(beta_rad)
    sinlambda = (np.sin(delta_rad) * np.sin(obliq) +
                 np.cos(delta_rad) * np.cos(obliq) * np.sin(alpha_rad)) / np.cos(beta_rad)
    lambda_rad = np.arctan2(sinlambda, coslambda)  # make sure we get the right quadrant
    lambda_rad = _wrap_to_2pi(lambda_rad)
    return lambda_rad, beta_rad
