# v_bac
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/transform/cumavg.py, line 55
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def v_bac(v, rho, depth):
    """
    Cumulative Backus average of a velocity log. You must provide
    either a depth or a time basis for the log.

    For a non-cumulative version that can also provide sclaing for the
    V_s log, as well as quality factor, see bruges.anisotropy.backus.

    Args:
        v (ndarray): The velocity log.
        rho (ndarray): The density log.
        depth (ndarray): The depth values corresponding to the logs.

    Returns:
        ndarray: The V_bac log.
    """
    num = np.cumsum(depth**2)
    den = np.cumsum(rho * depth) * np.cumsum(depth/(v**2 * rho))
    return np.sqrt(num / den)
