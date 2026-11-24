# double1d
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/plot/gmtpy.py, line 1633
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def double1d(a):
    a2 = num.empty(a.size*2-1)
    a2[::2] = a
    a2[1::2] = (a[:-1] + a[1:])/2.
    return a2
