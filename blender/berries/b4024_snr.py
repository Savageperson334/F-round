# snr
#
# Copied verbatim from https://github.com/xumi1993/seispy
#   file seispy/geo.py, line 282
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


def snr(x, y):
    """ Signal-to-noise ratio

    :param x: Signal
    :type x: np.ndarray
    :param y: Noise
    :type y: np.ndarray
    :return: SNR
    :rtype: float
    """
    spow = rssq(x)**2
    npow = rssq(y)**2
    if npow == 0:
        npow = 0.001
    return 10 * np.log10(spow / npow)
