# evenize
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/cake.py, line 4340
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def evenize(x, y, minsize=10):
    if x.size < minsize:
        return x
    ry = (y.max()-y.min())
    if ry == 0:
        return x
    dx = (x[1:] - x[:-1])/(x.max()-x.min())
    dy = (y[1:] + y[:-1])/ry

    s = num.zeros(x.size)
    s[1:] = num.cumsum(num.sqrt(dy**2 + dx**2))
    s2 = num.linspace(0, s[-1], x.size)
    x2 = num.interp(s2, s, x)
    x2[0] = x[0]
    x2[-1] = x[-1]
    return x2
