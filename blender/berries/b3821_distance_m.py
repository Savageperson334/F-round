# distance_m
#
# Copied verbatim from https://github.com/topherchris420/nocturne
#   file vdl7/skyglow.py, line 260
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def distance_m(lat0: float, lon0: float, lat1: float, lon1: float) -> float:
    """Equirectangular distance: exact enough across a city."""
    kx = 111_320.0 * math.cos(math.radians((lat0 + lat1) / 2))
    return math.hypot((lon1 - lon0) * kx, (lat1 - lat0) * 110_574.0)
