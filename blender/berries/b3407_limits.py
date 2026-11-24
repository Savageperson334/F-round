# limits
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/plot/smartplot.py, line 83
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def limits(points):
    lims = num.zeros((3, 2))
    if points.size != 0:
        lims[:, 0] = num.min(points, axis=0)
        lims[:, 1] = num.max(points, axis=0)

    return lims
