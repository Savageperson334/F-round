# get_distance_for_height_above_ground
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/atmosphere/models.py, line 204
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np

r_e = 6.371 * 1e6


def get_distance_for_height_above_ground(h, zenith, observation_level=0):
    """ inverse of get_height_above_ground() """
    r = r_e + observation_level
    return (h ** 2 + 2 * r * h + r ** 2 * np.cos(zenith) ** 2) ** 0.5 - r * np.cos(zenith)
