# sinc2
#
# Copied verbatim from https://github.com/agilescientific/in-bruges
#   notebook notebooks_dev/Wavelets.ipynb (its code cells joined in order; line 369 of those)
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def sinc2(duration, dt, f):
    t = np.arange(-duration/2., duration/2., dt)
    return t, np.sinc(0.5*np.pi*f*t)
