# neighbors
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/icosphere.py, line 102
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def neighbors(vertices, faces):

    nv = vertices.shape[0]
    nf, nc = faces.shape
    fedges = num.zeros((nf*nc, 2), dtype=int)
    for ic in range(nc):
        fedges[ic::nc, :] = faces[:, (ic, (ic+1) % nc)]

    indface = num.repeat(num.arange(nf), nc)
    fedges1 = fedges[:, 0] + fedges[:, 1]*nv
    sortorder = fedges1.argsort()
    fedges1_rev = fedges[:, 1] + fedges[:, 0]*nv

    inds = num.searchsorted(fedges1, fedges1_rev, sorter=sortorder)
    # todo: handle cases without neighbors
    assert num.all(fedges1[sortorder[inds]] == fedges1_rev)
    neighbors = indface[sortorder[inds]].reshape((nf, nc))
    return neighbors
