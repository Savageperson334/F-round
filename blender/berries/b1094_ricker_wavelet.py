# ricker_wavelet
#
# Copied verbatim from https://github.com/aradfarahani/Seismology
#   notebook AUT/Dr. Javaherian/2nd project_ES_03-04_1st term (2).ipynb (its code cells joined in order; line 20 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def ricker_wavelet(frequency, dt, length):
    t = np.arange(-length/2, length/2, dt)
    wavelet = (1 - 2 * (np.pi * frequency * t) ** 2) * np.exp(-(np.pi * frequency * t) ** 2)
    return wavelet
