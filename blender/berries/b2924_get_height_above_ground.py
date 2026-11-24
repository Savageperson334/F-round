# get_height_above_ground
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/atmosphere/models.py, line 196
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np

r_e = 6.371 * 1e6


def get_height_above_ground(d, zenith, observation_level=0):
    """ returns the perpendicular height above ground for a distance d from ground at a given zenith angle """
    r = r_e + observation_level
    x = d * np.sin(zenith)
    y = d * np.cos(zenith) + r
    return (x ** 2 + y ** 2) ** 0.5 - r
