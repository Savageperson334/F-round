# has_same_direction
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/helper.py, line 652
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def get_angle(v1, v2):
    """
    Calculates the angle between two vectors.

    Parameters
    ----------
    v1: 3d array or list of 3d arrays
        vector(s) one
    v2: 3d array
        vector two

    Returns: float or list of floats
        angle(s) between vector(s)
    """

    if v1.ndim == 2 and v2.ndim == 2:
        arccos = np.array([
            np.dot(v1_, v2_) / (np.linalg.norm(v1_.T, axis=0) * np.linalg.norm(v2_.T, axis=0))
            for v1_, v2_ in zip(v1, v2)])
    else:
        arccos = np.dot(v1, v2) / (np.linalg.norm(v1.T, axis=0) * np.linalg.norm(v2.T, axis=0))
    # catch numerical overlow
    mask1 = arccos > 1
    mask2 = arccos < -1
    mask = np.logical_or(mask1, mask2)
    if (type(mask) != np.bool_):
        arccos[mask1] = 1
        arccos[mask2] = -1
    else:
        if (mask1):
            arccos = 1
        if (mask2):
            arccos = -1
    return np.arccos(arccos)


def spherical_to_cartesian(zenith, azimuth):
    sinZenith = np.sin(zenith)
    x = sinZenith * np.cos(azimuth)
    y = sinZenith * np.sin(azimuth)
    z = np.cos(zenith)

    if hasattr(zenith, '__len__') and hasattr(azimuth, '__len__'):
        return np.array([x, y, z]).T
    else:
        return np.array([x, y, z])


def has_same_direction(zenith1, azimuth1, zenith2, azimuth2, distancecut=20):
    distancecut = np.deg2rad(distancecut)
    axis1 = spherical_to_cartesian(zenith1, azimuth1)
    axis2 = spherical_to_cartesian(zenith2, azimuth2)

    diff = get_angle(axis1, axis2)
    if (diff < distancecut):
        return True
    else:
        return False
