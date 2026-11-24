# estimate_beta_positive
#
# Copied verbatim from https://github.com/lmizrahi/etas
#   file etas/mc_b_est.py, line 56
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


def estimate_beta_positive(magnitudes: np.ndarray, delta_m: float = 0
                           ) -> tuple[float, float]:
    """ returns the b-value estimation using the positive differences of the
    Magnitudes

    Source:
        Van der Elst 2021 (J Geophysical Research: Solid Earth, Vol 126, Issue
        2)

    Args:
        magnitudes: vector of magnitudes differences, sorted in time (first
                    entry is the earliest earthquake)
        delta_m:    discretization of magnitudes. default is no discretization

    Returns:
        beta:       maximum likelihood beta (b_value = beta * log10(e))
    """
    mag_diffs = np.diff(magnitudes)
    # only take the values where the next earthquake is larger
    mag_diffs = abs(mag_diffs[mag_diffs > 0])
    beta = estimate_beta_tinti(mag_diffs, mc=delta_m, delta_m=delta_m)

    return beta
