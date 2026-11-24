# gaussFilter
#
# Copied verbatim from https://github.com/xumi1993/seispy
#   file seispy/decon.py, line 10
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def gaussFilter(dt, nft, f0):
    """
    Gaussian filter in frequency domain.

    :param dt: sample interval in second
    :type dt: float
    :param nft: number of samples
    :type nft: int
    :param f0: Gauss factor
    :type f0: float

    :return: Gaussian filter in frequency domain
    :rtype: np.ndarray
    """
    df = 1.0 / (nft * dt)
    nft21 = 0.5 * nft + 1
    f = df * np.arange(0, nft21)
    w = 2 * np.pi * f

    gauss = np.zeros([nft, 1])
    gauss1 = np.exp(-0.25 * (w / f0) ** 2) / dt
    gauss1.shape = (len(gauss1), 1)
    gauss[0:int(nft21)] = gauss1
    gauss[int(nft21):] = np.flipud(gauss[1:int(nft21) - 1])
    gauss = gauss[:, 0]

    return gauss
