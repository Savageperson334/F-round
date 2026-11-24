# tauCalcSWxy
#
# Copied verbatim from https://github.com/uafgeotools/array_processing
#   file array_processing/tools/generic.py, line 355
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def tauCalcSWxy(vel, xy, rij):
    r"""
    Calculates theoretical tau vector for a spherical wave moving across an
    array of ``n`` elements.

    Args:
        vel (float): Signal velocity across array
        xy: ``(d, )`` array; source location as 2-D [easting, northing] or 3-D
            [easting, northing, elevation] coordinates
        rij: ``(d, n)`` array; ``n`` element coordinates as [easting, northing,
            {elevation}] column vectors in ``d`` dimensions

    Returns:
        ``(n(n-1)//2, )`` array; time delays of relative signal arrivals (TDOA)
        for all unique sensor pairings
    """

    dim, nTraces = len(rij), len(rij[0])
    if dim == 2:
        rij = np.vstack((rij, [0] * nTraces))
    else:
        rij = np.vstack((rij,))
    if len(xy) == 2:
        xy0 = 0
    else:
        xy0 = []
    source = np.hstack((xy, xy0))
    idx = [(i, j) for i in range(rij.shape[1] - 1) for j in range(i + 1, rij.shape[1])]
    tau2sensor = (
        np.linalg.norm(rij - np.tile(source, nTraces).reshape(nTraces, 3).T, 2, axis=0)
        / vel
    )

    return tau2sensor[[j[1] for j in idx]] - tau2sensor[[i[0] for i in idx]]
