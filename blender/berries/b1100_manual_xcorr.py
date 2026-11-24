# manual_xcorr
#
# Copied verbatim from https://github.com/aradfarahani/Seismology
#   notebook UT/Dr. Siahkoohi/DSP/HW2.ipynb (its code cells joined in order; line 209 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def manual_xcorr(x, y):

    x = np.asarray(x)
    y = np.asarray(y)

    Nx = len(x)
    Ny = len(y)
    out_len = Nx + Ny - 1

    corr = np.zeros(out_len)

    # Flip y for cross-correlation
    y_flip = y[::-1]

    # Compute correlation
    for n in range(out_len):
        total = 0.0
        for k in range(Nx):
            j = n - k
            if 0 <= j < Ny:
                total += x[k] * y_flip[j]
        corr[n] = total

    return corr
