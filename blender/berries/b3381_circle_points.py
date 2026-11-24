# circle_points
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/plot/beachball.py, line 267
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def circle_points(aphi, sign=1.0):
    vecs = num.empty((aphi.size, 3), dtype=num.float64)
    vecs[:, 0] = num.cos(sign*aphi)
    vecs[:, 1] = num.sin(sign*aphi)
    vecs[:, 2] = 0.0
    return vecs
