# guess_vals
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/plot/gmtpy.py, line 1537
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def guess_vals(asorted):
    eps = (asorted[-1]-asorted[0])/asorted.size
    indis = num.nonzero(asorted[1:] - asorted[:-1] >= eps)[0]
    indis = num.concatenate((num.array([0]), indis+1,
                             num.array([asorted.size])))
    asum = num.zeros(asorted.size+1)
    asum[1:] = num.cumsum(asorted)
    return (asum[indis[1:]] - asum[indis[:-1]]) / (indis[1:]-indis[:-1])
