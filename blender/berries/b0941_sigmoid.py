# sigmoid
#
# Copied verbatim from https://github.com/agilescientific/in-bruges
#   notebook notebooks_dev/Wedges_3D.ipynb (its code cells joined in order; line 44 of those)
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def sigmoid(start, stop, num):
    """
    Nonlinear space following a logistic function.

    The function is asymptotic; the parameters used in the sigmoid
    gets within 0.5% of the target thickness in a wedge increasing
    from 0 to 2x the original thickness.
    """
    x = np.linspace(-5.293305, 5.293305, num)
    return start + (stop-start) / (1 + np.exp(-x))
