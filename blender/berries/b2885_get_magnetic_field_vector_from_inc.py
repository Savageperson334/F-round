# get_magnetic_field_vector_from_inc
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/helper.py, line 419
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def get_magneticfield_azimuth(magnetic_field_declination):
    """Convert a declination to a local azimuth"""
    return np.pi / 2 - magnetic_field_declination


def get_magneticfield_zenith(magnetic_field_inclination):
    """
    Convert an inclination to a local zenith
    """
    return np.pi / 2 - magnetic_field_inclination


def spherical_to_cartesian(zenith, azimuth):
    sinZenith = np.sin(zenith)
    x = sinZenith * np.cos(azimuth)
    y = sinZenith * np.sin(azimuth)
    z = np.cos(zenith)

    if hasattr(zenith, '__len__') and hasattr(azimuth, '__len__'):
        return np.array([x, y, z]).T
    else:
        return np.array([x, y, z])


def get_magnetic_field_vector_from_inc(inclination, declination):
    """
    Get the magnetic field from its inclination and declination

    Returns the (normalized) magnetic field direction from its
    inclination and declination.
    """
    return spherical_to_cartesian(get_magneticfield_zenith(inclination),
                                  get_magneticfield_azimuth(declination))
