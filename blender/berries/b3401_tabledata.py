# tabledata
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/plot/gmtpy.py, line 1625
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def tabledata(xf, yf, zf):
    assert yf.size, xf.size == zf.shape
    x = num.tile(xf, yf.size)
    y = num.repeat(yf, xf.size)
    z = zf.flatten()
    return x, y, z
