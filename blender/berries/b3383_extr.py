# extr
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/plot/beachball.py, line 458
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def extr(points):
    pmean = num.mean(points, axis=0)
    return points + pmean*0.05
