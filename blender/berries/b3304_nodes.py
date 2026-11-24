# nodes
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/gf/meta.py, line 3083
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def nodes(xs):
    ns = [x.size for x in xs]
    nnodes = num.prod(ns)
    ndim = len(xs)
    nodes = num.empty((nnodes, ndim), dtype=xs[0].dtype)
    for idim in range(ndim-1, -1, -1):
        x = xs[idim]
        nrepeat = num.prod(ns[idim+1:], dtype=int)
        ntile = num.prod(ns[:idim], dtype=int)
        nodes[:, idim] = num.repeat(num.tile(x, ntile), nrepeat)

    return nodes
