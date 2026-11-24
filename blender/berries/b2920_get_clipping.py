# get_clipping
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/analyses/radiationenergy.py, line 31
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def get_clipping(dxmax):
    """ get clipping correction

    Parameters
    ----------
    dxmax : float
        distance to shower maximum in g/cm^2

    Returns
    -------
    float
        fraction of radiation energy that is radiated in the atmosphere

    """
    return 1 - np.exp(-8.7 * (dxmax * 1e-3 + 0.29) ** 1.89)
