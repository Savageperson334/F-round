# estimate_beta_tinti
#
# Copied verbatim from https://github.com/lmizrahi/etas
#   file etas/mc_b_est.py, line 39
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def estimate_beta_tinti(magnitudes, mc, weights=None, axis=None, delta_m=0):
    """
    Tinti, S., & Mulargia, F. (1987). Confidence intervals of b values
    for grouped magnitudes. Bulletin of the Seismological Society of
    America, 77(6), 2125-2134.
    """

    if delta_m > 0:
        p = (1 + (delta_m / (np.average(
            magnitudes - mc, weights=weights, axis=axis))))
        beta = 1 / delta_m * np.log(p)
    else:
        beta = 1 / np.average((magnitudes - (mc - delta_m / 2)),
                              weights=weights, axis=axis)
    return beta
