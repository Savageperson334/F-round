# blockmean
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/plot/gmtpy.py, line 1547
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def blockmean(asorted, b):
    indis = num.nonzero(asorted[1:] - asorted[:-1])[0]
    indis = num.concatenate((num.array([0]), indis+1,
                             num.array([asorted.size])))
    bsum = num.zeros(b.size+1)
    bsum[1:] = num.cumsum(b)
    return (
        asorted[indis[:-1]],
        (bsum[indis[1:]] - bsum[indis[:-1]]) / (indis[1:]-indis[:-1]))
