# tune
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/sampler/smc.py, line 560
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def tune(acc_rate):
    """
    Tune adaptively based on the acceptance rate.

    Parameters
    ----------
    acc_rate: scalar, float
        Acceptance rate of the Metropolis sampling

    Returns
    -------
    scaling: scalar float
    """

    # a and b after Muto & Beck 2008 .
    a = 1.0 / 9
    b = 8.0 / 9
    return np.power((a + (b * acc_rate)), 2)
    return np.power((a + (b * acc_rate)), 2)
