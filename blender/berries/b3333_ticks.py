# ticks
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/gui/sparrow/elements/grid.py, line 34
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def ticks(vmin, vmax, vstep):
    vmin = num.floor(vmin / vstep) * vstep
    vmax = num.ceil(vmax / vstep) * vstep
    n = int(round((vmax - vmin) / vstep))
    return vmin + num.arange(n+1) * vstep
