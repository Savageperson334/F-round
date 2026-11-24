# ecef_to_wgs84
#
# Copied verbatim from https://github.com/projecthorus/sondehub-decoders
#   file sondehubdecoders/utils/gnss_helpers.py, line 15
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import atan2
from math import cos
from math import pi
from math import sin
from math import sqrt

WGS84_EARTH_a = 6378137.0

WGS84_EARTH_b = 6356752.31424518

WGS84_EARTH_a2_b2 = (WGS84_EARTH_a * WGS84_EARTH_a - WGS84_EARTH_b * WGS84_EARTH_b)

WGS84_EARTH_e2 = WGS84_EARTH_a2_b2 / (WGS84_EARTH_a * WGS84_EARTH_a)

WGS84_EARTH_ee2 = WGS84_EARTH_a2_b2 / (WGS84_EARTH_b * WGS84_EARTH_b)


def ecef_to_wgs84(ecef_x_m, ecef_y_m, ecef_z_m):
    """ 
    Convert ECEF coordinates (m) to lat/lon/alt in a WGS84 datum 
    Ported from ecef2elli from rs41mod.c
    """

    lam = atan2( ecef_y_m, ecef_x_m )

    p = sqrt( ecef_x_m * ecef_x_m + ecef_y_m * ecef_y_m)
    t = atan2( ecef_z_m * WGS84_EARTH_a , p * WGS84_EARTH_b)

    phi = atan2( 
        ecef_z_m + WGS84_EARTH_ee2 * WGS84_EARTH_b * sin(t)*sin(t)*sin(t),
        p - WGS84_EARTH_e2 * WGS84_EARTH_a * cos(t)*cos(t)*cos(t)
    )

    R = WGS84_EARTH_a / sqrt( 1 - WGS84_EARTH_e2*sin(phi)*sin(phi))

    alt = p / cos(phi) - R
    lat = phi * 180/pi
    lon = lam * 180/pi

    return (lat, lon, alt)
