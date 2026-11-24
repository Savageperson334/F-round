# gabor
#
# Copied verbatim from https://github.com/agilescientific/in-bruges
#   notebook notebooks_dev/Wavelets.ipynb (its code cells joined in order; line 259 of those)
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from collections import namedtuple
import numpy as np


def gabor(duration, dt, f, return_t=False):
    f = np.asanyarray(f).reshape(-1, 1)
    t = np.arange(-duration/2, duration/2, dt)

    ft = f * t
    w = np.exp(-2 * ft**2) * np.cos(2 * np.pi * ft)

#     gauss = scipy.signal.gaussian()
    w = np.squeeze(w)

    if return_t:
        GaborWavelet = namedtuple('GaborWavelet', ['amplitude', 'time'])
        return GaborWavelet(w, t)
    else:
        return w
