# cosd
#
# Copied verbatim from https://github.com/xumi1993/seispy
#   file seispy/geo.py, line 18
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def cosd(deg):
    """ Cosine function with degree as input

    :param deg: Degree
    :type deg: float
    :return: Cosine value
    :rtype: float
    """
    rad = np.radians(deg)
    return np.cos(rad)
