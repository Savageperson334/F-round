# min_max_normalization
#
# Copied verbatim from https://github.com/seisbench/seisbench
#   file seisbench/util/torch_helpers.py, line 23
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def min_max_normalization(x: np.array, eps: float = 1e-10) -> np.array:
    """
    Min-max normalize a numpy array, i.e. values are in the range [0, 1].

    :param x: numpy array of arbitrary shape
    :param eps: Float to avoid division by zeros
    :return: min-max normalized input array
    """
    return (x - np.min(x)) / (np.max(x) - np.min(x) + eps)
