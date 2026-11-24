# manual_autocorr
#
# Copied verbatim from https://github.com/aradfarahani/Seismology
#   notebook UT/Dr. Siahkoohi/DSP/HW2.ipynb (its code cells joined in order; line 42 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def manual_autocorr(x):

    x = np.asarray(x)
    N = len(x)
    maxlag = N - 1
    lags = np.arange(-maxlag, maxlag + 1)
    ac = np.zeros_like(lags, dtype=float)

    for idx, k in enumerate(lags):
        if k >= 0:
            overlap = N - k
            ac[idx] = np.sum(x[:overlap] * x[k:k+overlap])
        else:
            k2 = -k
            overlap = N - k2
            ac[idx] = np.sum(x[k2:k2+overlap] * x[:overlap])
    return lags, ac
