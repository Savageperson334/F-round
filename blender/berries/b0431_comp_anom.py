# comp_anom
#
# Copied verbatim from https://github.com/KMFleischer/PyEarthScience
#   file Tutorial/lib/dkrz_utils.py, line 153
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def comp_anom(data):
    """Compute the anomaly of data.
       Input parameter:   scalar or array
    """
    return((data-np.mean(data)))
