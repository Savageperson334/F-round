# filledi
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/gf/meta.py, line 3097
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def filledi(x, n):
    a = num.empty(n, dtype=int)
    a.fill(x)
    return a
