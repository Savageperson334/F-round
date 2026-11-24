# nvals
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/plot/gmtpy.py, line 1532
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def nvals(asorted):
    eps = (asorted[-1]-asorted[0])/asorted.size
    return num.sum(asorted[1:] - asorted[:-1] >= eps) + 1
