# moving_avg
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/trace.py, line 3627
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def moving_avg(x, n):
    n = int(n)
    cx = x.cumsum()
    nn = len(x)
    y = num.zeros(nn, dtype=cx.dtype)
    y[n//2:n//2+(nn-n)] = (cx[n:]-cx[:-n])/n
    y[:n//2] = y[n//2]
    y[n//2+(nn-n):] = y[n//2+(nn-n)-1]
    return y
