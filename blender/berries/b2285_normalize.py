# normalize
#
# Copied verbatim from https://github.com/interactive-sonification/pya
#   file pya/helper/helpers.py, line 46
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sound sonification
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def normalize(d):
    """Return the normalized input array"""
    # d is a (n x dimension) np array
    d -= np.min(d, axis=0)
    d /= np.ptp(d, axis=0)
    return d
