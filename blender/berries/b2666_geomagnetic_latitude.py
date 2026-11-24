# geomagnetic_latitude
#
# Copied verbatim from https://github.com/mbeher2200/DarkHours
#   file darkhours/aurora.py, line 126
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

GM_POLE_LAT = 80.8

GM_POLE_LON = -72.7


def geomagnetic_latitude(lat: float, lon: float) -> float:
    """Signed geomagnetic latitude (degrees) via the centered-dipole formula."""
    lat_r  = math.radians(lat)
    pole_r = math.radians(GM_POLE_LAT)
    dlon_r = math.radians(lon - GM_POLE_LON)
    s = (math.sin(lat_r) * math.sin(pole_r)
         + math.cos(lat_r) * math.cos(pole_r) * math.cos(dlon_r))
    return math.degrees(math.asin(max(-1.0, min(1.0, s))))
