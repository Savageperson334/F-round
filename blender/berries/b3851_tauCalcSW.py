# tauCalcSW
#
# Copied verbatim from https://github.com/uafgeotools/array_processing
#   file array_processing/tools/generic.py, line 314
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def tauCalcSW(vel, rAzPhi, rij):
    r"""
    Calculates theoretical tau vector for a spherical wave moving across an
    array of ``n`` elements.

    Args:
        vel (float): Signal velocity across array
        rAzPhi: Range to source and back azimuth from co-array coordinate
            origin (° CW from N); range to source, back azimuth and elevation
            angle from co-array coordinate origin (° CW from N, ° from N-E
            plane)
        rij: ``(d, n)`` array; ``n`` element coordinates as [easting, northing,
            {elevation}] column vectors in ``d`` dimensions

    Returns:
        ``(n(n-1)//2, )`` array; time delays of relative signal arrivals (TDOA)
        for all unique sensor pairings
    """

    dim, nTraces = rij.shape
    if dim == 2:
        rij = np.vstack((rij, np.zeros((1, nTraces))))
    if len(rAzPhi) == 3:
        phi = rAzPhi[2] / 180 * np.pi
    else:
        phi = 0
    idx = [(i, j) for i in range(rij.shape[1] - 1) for j in range(i + 1, rij.shape[1])]
    # aw, this is so convolutedly elegant that it must be saved in a
    # comment for posterity!, but the line below it is "simpler"
    # az = -( (rAzPhi[1]/180*pi - 2*pi)%(2*pi) - pi/2  )%(2*pi)
    az = np.pi * (-rAzPhi[1] / 180 + 0.5)
    source = rAzPhi[0] * np.array([np.cos(az), np.sin(az), np.sin(phi)])
    source[:-1] *= np.cos(phi)
    tau2sensor = (
        np.linalg.norm(rij - np.tile(source, nTraces).reshape(nTraces, 3).T, 2, axis=0)
        / vel
    )

    return tau2sensor[[j[1] for j in idx]] - tau2sensor[[i[0] for i in idx]]
