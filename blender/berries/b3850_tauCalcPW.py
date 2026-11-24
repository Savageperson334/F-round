# tauCalcPW
#
# Copied verbatim from https://github.com/uafgeotools/array_processing
#   file array_processing/tools/generic.py, line 278
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def tauCalcPW(vel, azPhi, rij):
    r"""
    Calculates theoretical tau vector for a plane wave moving across an array
    of ``n`` elements.

    Args:
        vel (float): Signal velocity across array
        azPhi: Back azimuth (float) from co-array coordinate origin (° CW from
            N); back azimuth and elevation angle (array) from co-array
            coordinate origin (° CW from N, ° from N-E plane)
        rij: ``(d, n)`` array; ``n`` element coordinates as [easting, northing,
            {elevation}] column vectors in ``d`` dimensions

    Returns:
        ``(n(n-1)//2, )`` array; time delays of relative signal arrivals (TDOA)
        for all unique sensor pairings
    """

    dim, nTraces = rij.shape
    if dim == 2:
        rij = np.vstack((rij, np.zeros((1, nTraces))))
    idx = [(i, j) for i in range(rij.shape[1] - 1) for j in range(i + 1, rij.shape[1])]
    X = rij[:, [i[0] for i in idx]] - rij[:, [j[1] for j in idx]]
    if np.isscalar(azPhi):
        phi = 0
        az = azPhi
    else:
        phi = azPhi[1] / 180 * np.pi
        az = azPhi[0]
    az = np.pi * (-az / 180 + 0.5)
    s = np.array([np.cos(az), np.sin(az), np.sin(phi)])
    s[:-1] *= np.cos(phi)

    return X.T @ (s / vel)
