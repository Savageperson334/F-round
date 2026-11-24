# sinc
#
# Copied verbatim from https://github.com/agilescientific/in-bruges
#   notebook notebooks_dev/Wavelets.ipynb (its code cells joined in order; line 323 of those)
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np
from collections import namedtuple


def generic(func, duration, dt, f, return_t=False, taper='blackman'):
    f = np.asanyarray(f).reshape(-1, 1)
    t = np.arange(-duration/2., duration/2., dt)
    t[t == 0] = 1e-12  # Avoid division by zero.
    f[f == 0] = 1e-12  # Avoid division by zero.

    w = np.squeeze(func(t, f))

    if taper:
        tapers = {
            'bartlett': np.bartlett,
            'blackman': np.blackman,
            'hamming': np.hamming,
            'hanning': np.hanning,
            'none': lambda _: 1,
        }
        taper = tapers.get(taper, taper)
        w *= taper(t.size)

    if return_t:
        Wavelet = namedtuple('Wavelet', ['amplitude', 'time'])
        return Wavelet(w, t)
    else:
        return w


def sinc(duration, dt, f, return_t=False, taper='blackman'):
    """
    Plain sinc function, tapered.
    """
    func = lambda t_, f_: np.squeeze(np.sin(2*np.pi*f_*t_) / (2*np.pi*f_*t_))
    return generic(func, duration, dt, f, return_t, taper)
