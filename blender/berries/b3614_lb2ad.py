# lb2ad
#
# Copied verbatim from https://github.com/spacetelescope/jwst_coronagraph_visibility
#   file jwst_coronagraph_visibility/skyvec2ins.py, line 166
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


def lb2ad(lambda_rad, beta_rad):
    """Convert ecliptic coordinates (lambda, beta) to equatorial coordinates (RA, Dec, i.e. alpha, delta)
    according to Eq 4 in Leinert et al. 1998.

    Parameters
    ----------
    lambda_rad : ndarray
        Ecliptic longitude in radians.
    beta_rad : numpy.ndarray
        Ecliptic latitude in radians.

    Returns
    -------
    alpha : ndarray
        Equatorial Right Ascension in radians.
    delta : ndarray
        Equatorial Declination in radians.
    """
    obliq = _tenv(23, 26, 21.45)  # J2000 obliquity of Earth in degrees
    obliq *= np.pi / 180.

    delta = np.arcsin(np.sin(beta_rad) * np.cos(obliq) + np.cos(beta_rad) * np.sin(obliq) * np.sin(lambda_rad))
    cosalpha = np.cos(lambda_rad) * np.cos(beta_rad) / np.cos(delta)
    sinalpha = (-np.sin(beta_rad) * np.sin(obliq) +
                np.cos(beta_rad) * np.cos(obliq) * np.sin(lambda_rad)) / np.cos(delta)
    alpha = np.arctan2(sinalpha, cosalpha)
    alpha = _wrap_to_2pi(alpha)

    return alpha, delta
