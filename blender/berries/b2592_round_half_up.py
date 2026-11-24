# round_half_up
#
# Copied verbatim from https://github.com/lmizrahi/etas
#   file etas/mc_b_est.py, line 22
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def round_half_up(n, decimals=0):
    # this is because numpy does weird rounding.
    """Round half up (``0.15 -> 0.2``), unlike numpy's round-half-to-even.

    Parameters
    ----------
    n : float or array-like
    decimals : int, default 0

    Returns
    -------
    float or array-like
    """
    multiplier = 10 ** decimals
    return np.floor(n * multiplier + 0.5) / multiplier
