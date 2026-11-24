# get_magneticfield_azimuth
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/helper.py, line 390
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
