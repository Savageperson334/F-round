# shannon2
#
# Copied verbatim from https://github.com/agilescientific/in-bruges
#   notebook notebooks_dev/Wavelets.ipynb (its code cells joined in order; line 375 of those)
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def shannon2(duration, dt, f):
    t = np.arange(-duration/2., duration/2., dt)
    return t, 2 * np.sinc(2*np.pi*f*t - 1) - np.sinc(2*np.pi*f*t)
