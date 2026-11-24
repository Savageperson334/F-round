# get_sine_angle_to_lorentzforce
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/helper.py, line 439
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


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


def get_lorentzforce_vector(zenith, azimuth, magnetic_field_vector=None):
    if (magnetic_field_vector is None):
        magnetic_field_vector = get_magnetic_field_vector()
    showerAxis = spherical_to_cartesian(zenith, azimuth)
    magnetic_field_vector_normalized = magnetic_field_vector / \
        np.linalg.norm(magnetic_field_vector.T, axis=0, keepdims=True).T
    return np.cross(showerAxis, magnetic_field_vector_normalized)


def get_sine_angle_to_lorentzforce(zenith, azimuth, magnetic_field_vector=None):
    # we use the tanspose of the vector or matrix to be able to always use
    # axis=0
    return np.linalg.norm(get_lorentzforce_vector(zenith, azimuth, magnetic_field_vector).T, axis=0)
