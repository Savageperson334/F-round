# asind
#
# Copied verbatim from https://github.com/xumi1993/seispy
#   file seispy/geo.py, line 54
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def asind(x):
    """ Inverse sine function with degree as output

    :param x: Sine value
    :type x: float
    :return: Degree
    :rtype: float
    """
    rad = np.arcsin(x)
    return np.degrees(rad)
