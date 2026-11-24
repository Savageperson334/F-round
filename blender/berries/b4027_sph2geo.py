# sph2geo
#
# Copied verbatim from https://github.com/xumi1993/seispy
#   file seispy/geo.py, line 433
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def rad2deg(rad):
    """ Convert radian to degree

    :param rad: Radian
    :type rad: float
    :return: Degree
    :rtype: float
    """
    deg = rad*(360/(2*np.pi))
    return deg


def sph2geo(r, theta, phi):
    """
    Convert spherical coordinates to geographic coordinates.

    :param float r: radial distance from coordinate system origin
                    {**Units**: km, **Range**: [0, inf)}
    :param float theta: polar angle {**Units**: radians, **Range**: [0,
                        π]}
    :param float phi: azimuthal angle {**Units**: radians, **Range**:
                      [-π, π]}
    :returns: geographic coordinate conversion *(lat, lon, depth)* of
              spherical coordinates
    :rtype: (float, float, float)
    """
    z = 6371 - r
    lat = 90 - rad2deg(theta)
    lon = rad2deg(phi)
    return z, lat, lon
