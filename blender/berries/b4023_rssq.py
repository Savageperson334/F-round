# rssq
#
# Copied verbatim from https://github.com/xumi1993/seispy
#   file seispy/geo.py, line 272
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def rssq(x):
    """ Root sum square
    :param x: Input array
    :type x: np.ndarray
    :return: Root sum square
    :rtype: float
    """
    return np.sqrt(np.sum(x**2)/len(x))
