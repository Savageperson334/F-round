# earth_radius
#
# Copied verbatim from https://github.com/pnuu/pyBalloon
#   file pyb_aux.py, line 31
#   licence (as GitHub reports it): LGPL-3.0   see ../licenses/
#   catalogue shelf: Weather balloon telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def earth_radius(lat_rad):
    """Calculate Earth WGS84 based radius on a given latitude.

    http://en.wikipedia.org/wiki/Earth_radius#Radius_at_a_given_geodetic_latitude
    """

    # WGS84 reference ellipsoid
    a = 6378.137     # Earth equatorial radius, km
    b = 6356.7523142 # Earth polar radius, km

    cos_lat = np.cos(lat_rad)
    sin_lat = np.sin(lat_rad)

    r = np.sqrt(((a*a*cos_lat)**2 + (b*b*sin_lat)**2) / 
                ((a*cos_lat)**2 + (b*sin_lat)**2))

    return r
