# split_real_imag_channels
#
# Copied verbatim from https://github.com/polimi-ispl/nah-khcnn
#   file src/utils/data_processing.py, line 63
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def split_real_imag_channels(data):
    """
    Split complex image in two channels
    :param data: complex data
    :return: out_channels - data in two channels (real and imaginary parts)
    """
    real_img = np.copy(np.real(data))
    imag_img = np.copy(np.imag(data))

    out_channels = np.concatenate((real_img, imag_img), axis=-1)

    return out_channels
