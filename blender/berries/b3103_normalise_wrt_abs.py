# normalise_wrt_abs
#
# Copied verbatim from https://github.com/polimi-ispl/nah-khcnn
#   file src/utils/data_processing.py, line 11
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def normalise_wrt_abs(complex_data):
    """
    normalized complex_data wrt to max(abs)
    :param complex_data: numpy array
    :return:
    """
    data = complex_data.copy()
    data = data.reshape(data.shape[0], -1)
    M = np.max(abs(data), axis=-1).reshape(-1, 1)  # maximum for each images
    M = np.tile(M, (1, data.shape[-1]))
    data_norm = data / M

    data_norm = data_norm.reshape(complex_data.shape)

    return data_norm
