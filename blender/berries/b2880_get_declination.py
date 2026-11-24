# get_declination
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/helper.py, line 339
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def cartesian_to_spherical(x, y, z):
    # normlize vector
    norm = (x ** 2 + y ** 2 + z ** 2) ** 0.5
    x2 = x / norm
    y2 = y / norm
    z2 = z / norm
    theta = 0
    if hasattr(x, '__len__') and hasattr(y, '__len__')and hasattr(z, '__len__'):
        theta = np.zeros_like(x)
        theta[z2 < 1] = np.arccos(z2[z2 < 1])
        phi = np.arctan2(y2, x2)
        return theta, phi
    else:
        if (z2 < 1):
            theta = np.arccos(z2)
        phi = np.arctan2(y2, x2)
        return theta, phi


def get_declination(magnetic_field_vector):
    """
    Returns the declination of a vector.

    The declination is measured relative to the coordinate system
    y-axis (i.e. the second cartesian component), and positive for East,
    negative for West. Note that this means for coordinate systems that
    are not aligned with true North, this definition of declination
    does not agree with most other sources.

    Parameters
    ----------
    magnetic_field_vector : np.ndarray or list
        Vector in cartesian coordinates

    Returns
    -------
    declination : float
        The declination of the vector

    """
    zenith, azimuth = cartesian_to_spherical(*magnetic_field_vector)

    return np.pi / 2 - azimuth
