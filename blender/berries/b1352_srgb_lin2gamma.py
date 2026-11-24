# srgb_lin2gamma
#
# Copied verbatim from https://github.com/choisuyeon/sawh
#   file utils/utils.py, line 63
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def srgb_lin2gamma(im_in):
    """Convert from linear to sRGB color space."""
    thresh = 0.0031308
    im_out = np.where(
        im_in <= thresh,
        12.92 * im_in,
        1.055 * (im_in ** (1 / 2.4)) - 0.055,
    )
    return im_out
