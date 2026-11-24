# rick
#
# Copied verbatim from https://github.com/agilescientific/in-bruges
#   notebook notebooks_dev/Bruges_hacking.ipynb (its code cells joined in order; line 611 of those)
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from collections import namedtuple
import numpy as np


def rick(duration, dt, f, return_t=False):
    f = np.array(f).reshape((-1, 1))
    t = np.arange(-duration/2, duration/2, dt)
    pft2 = (np.pi * f * t)**2
    w = np.squeeze((1 - (2 * pft2)) * np.exp(-pft2))

    if return_t:
        RickerWavelet = namedtuple('RickerWavelet', ['amplitude', 'time'])
        return RickerWavelet(w, t)
    else:
        return w
