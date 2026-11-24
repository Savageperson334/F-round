# ricker_wavelet
#
# Copied verbatim from https://github.com/aradfarahani/Seismology
#   notebook UT/Dr. Bagheri/Seismic interpretation/Bagheri p1 s2.ipynb (its code cells joined in order; line 6 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def ricker_wavelet(f, dt, length):
    t = np.arange(-length/2, length/2, dt)
    y = (1 - 2 * (np.pi * f * t)**2) * np.exp(-(np.pi * f * t)**2)
    return y
