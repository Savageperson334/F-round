# len_deg_lat
#
# Copied verbatim from https://github.com/lermert/noisi
#   file noisi/util/geo.py, line 88
#   licence (as GitHub reports it): LGPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import cos
from math import pi


def len_deg_lat(lat):
    # This is the length of one degree of latitude
    # approx. after WGS84, between lat-0.5deg and lat+0.5 deg
    # in m
    lat = pi / 180 * lat
    dlat = 111132.954 - 559.822 * cos(2 * lat) + 1.175 * cos(4 * lat)
    return round(dlat, 5)
