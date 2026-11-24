# sigmoid
#
# Copied verbatim from https://github.com/timsainb/noisereduce
#   file noisereduce/spectralgate/utils.py, line 4
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def sigmoid(x, shift, mult):
    """
    Using this sigmoid to discourage one network overpowering the other
    """
    return 1 / (1 + np.exp(-(x + shift) * mult))
