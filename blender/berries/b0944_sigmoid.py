# sigmoid
#
# Copied verbatim from https://github.com/agilescientific/in-bruges
#   notebook notebooks_dev/Wedges_and_sigmoids_from_logs.ipynb (its code cells joined in order; line 7 of those)
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def sigmoid(x):
    """Logistic function.
    """
    return 2 / (1 + np.exp(-x))
