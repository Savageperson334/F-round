# ricker
#
# Copied verbatim from https://github.com/aradfarahani/Seismology
#   notebook AUT/Untitled15.ipynb (its code cells joined in order; line 17 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def ricker(f, length, dt):
    length = int(length / dt)  # Convert length to number of samples
    t = np.linspace(-length / 2, (length - 1) / 2, length) * dt
    y = (1.0 - 2.0 * (np.pi**2) * (f**2) * (t**2)) * np.exp(-(np.pi**2) * (f**2) * (t**2))
    return y
