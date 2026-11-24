# get_expected_efield_vector_vxB_vxvxB
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/helper.py, line 532
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


def get_magnetic_field_vector(site=None):
    """
    get the geomagnetic field vector in Gauss. x points to geographic East and y towards geographic North
    """
    magnetic_fields = {
        'auger': np.array([0.00871198, 0.19693423, 0.1413841]),
        'mooresbay': np.array([0.058457, -0.09042, 0.61439]),
        'summit': np.array([-.037467, 0.075575, -0.539887]),  # Summit station, Greenland
        'southpole': np.array([-0.14390398, 0.08590658, 0.52081228]),  # position of SP arianna station
        'lofar': np.array([0.004675, 0.186270, -0.456412])  # values from 2015
    }
    if site is None:
        site = 'auger'
    return magnetic_fields[site.lower()]


def spherical_to_cartesian(zenith, azimuth):
    sinZenith = np.sin(zenith)
    x = sinZenith * np.cos(azimuth)
    y = sinZenith * np.sin(azimuth)
    z = np.cos(zenith)

    if hasattr(zenith, '__len__') and hasattr(azimuth, '__len__'):
        return np.array([x, y, z]).T
    else:
        return np.array([x, y, z])


def get_angle_to_magnetic_field_vector(zenith, azimuth, site=None):
    """
        returns the angle between shower axis and magnetic field
    """
    magnetic_field = get_magnetic_field_vector(site=site)
    v = spherical_to_cartesian(zenith, azimuth)
    return get_angle(magnetic_field, v)


def get_expected_efield_vector_vxB_vxvxB(station_positions, zenith, azimuth, a=.14):
    """
    also returns the expected electric field vector, but station positions and
    the returned field vectors are in the vxB-vxvxB coordinate system
    """
    alpha = get_angle_to_magnetic_field_vector(zenith, azimuth)
    e_geomagnetic = np.array([-np.sin(alpha), 0, 0])
    e_charge_excess = -a * station_positions / np.linalg.norm(station_positions)
    return e_charge_excess + e_geomagnetic
