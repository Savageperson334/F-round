# xytups
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/cake.py, line 4386
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def xytups(xx, yy):
    d = []
    for x, y in zip(xx, yy):
        if num.isfinite(y):
            d.append((x, y))
    return d
