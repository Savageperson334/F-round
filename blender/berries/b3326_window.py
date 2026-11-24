# window
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/gui/snuffler/snufflings/ampspec.py, line 11
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def window(freqs, fc, b):
    w = num.zeros(len(freqs))
    if fc == 0.:
        w[freqs == 0.0] = 1.
        return w
    mask = num.logical_and(freqs != 0.0, freqs != fc)
    T = num.log10(freqs[mask]/fc)*b
    w[mask] = (num.sin(T)/T)**4
    w[freqs == fc] = 1.
    w /= num.sum(w)
    return w
