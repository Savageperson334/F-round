# look_bearing
#
# Copied verbatim from https://github.com/mbeher2200/DarkHours
#   file darkhours/aurora.py, line 136
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

GM_POLE_LAT = 80.8

GM_POLE_LON = -72.7


def look_bearing(lat: float, lon: float) -> float:
    """Great-circle initial bearing (° from true north) toward the dipole pole.

    Northern-hemisphere sites aim at the north dipole pole; southern sites aim
    at the south dipole pole — computed directly as a bearing to the antipode
    (−80.8°, +107.3°E), never as a flipped north-pole bearing, so a Tasmanian
    photographer is told to look ~S, not N.
    """
    if lat >= 0:
        pole_lat, pole_lon = GM_POLE_LAT, GM_POLE_LON
    else:
        pole_lat, pole_lon = -GM_POLE_LAT, GM_POLE_LON + 180.0

    lat1 = math.radians(lat)
    lat2 = math.radians(pole_lat)
    dlon = math.radians(pole_lon - lon)
    y = math.sin(dlon) * math.cos(lat2)
    x = (math.cos(lat1) * math.sin(lat2)
         - math.sin(lat1) * math.cos(lat2) * math.cos(dlon))
    return math.degrees(math.atan2(y, x)) % 360.0
