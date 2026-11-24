# z_score_normalization
#
# Copied verbatim from https://github.com/seisbench/seisbench
#   file seisbench/util/torch_helpers.py, line 34
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def z_score_normalization(x: np.array) -> np.array:
    """
    Normalize data by z-score.

    .. math::
        \frax{x - \mu}{\sigma}

    :param x: numpy array of arbitrary shape
    :return: normalized input array using z-score
    """
    return (x - np.mean(x)) / np.std(x)
