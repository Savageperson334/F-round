# magnitude
#
# Copied verbatim from https://github.com/donjpierce/traffic
#   file models.py, line 69
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def magnitude(vector):
    """ Returns the magnitude of a vector """
    return np.linalg.norm(vector)
