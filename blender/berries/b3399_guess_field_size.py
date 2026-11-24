# guess_field_size
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/plot/gmtpy.py, line 1575
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math
import numpy as num


def nvals(asorted):
    eps = (asorted[-1]-asorted[0])/asorted.size
    return num.sum(asorted[1:] - asorted[:-1] >= eps) + 1


def guess_field_size(x_sorted, y_sorted, z=None, mode=None):
    critical_fraction = 1./num.e - 0.014*3
    xs = x_sorted
    ys = y_sorted
    nxs, nys = nvals(xs), nvals(ys)
    if mode == 'nonrandom':
        return nxs, nys, 0
    elif xs.size == nxs*nys:
        # exact match
        return nxs, nys, 0
    elif nxs >= xs.size*critical_fraction and nys >= xs.size*critical_fraction:
        # possibly randomly sampled
        nxs = int(math.sqrt(xs.size))
        nys = nxs
        return nxs, nys, 2
    else:
        return nxs, nys, 1
