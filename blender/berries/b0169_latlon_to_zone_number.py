# latlon_to_zone_number
#
# Copied verbatim from https://github.com/EMob-Lab/MnMS
#   file script/conversion/bison/coordinates.py, line 34
#   licence (as GitHub reports it): LGPL-3.0   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def latlon_to_zone_number(latitude, longitude):

    if isinstance(latitude, np.ndarray):
        latitude = latitude.flat[0]
    if isinstance(longitude, np.ndarray):
        longitude = longitude.flat[0]

    if 56 <= latitude < 64 and 3 <= longitude < 12:
        return 32

    if 72 <= latitude <= 84 and longitude >= 0:
        if longitude < 9:
            return 31
        elif longitude < 21:
            return 33
        elif longitude < 33:
            return 35
        elif longitude < 42:
            return 37

    return int((longitude + 180) / 6) + 1
