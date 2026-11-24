# srgb_lin2gamma
#
# Copied verbatim from https://github.com/computational-imaging/neural-3d-holography
#   file utils.py, line 281
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#   the same function also appears in: computational-imaging/time-multiplexed-neural-holography
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def srgb_lin2gamma(im_in):
    """ converts from linear to sRGB color space """
    thresh = 0.0031308
    im_out = np.where(im_in <= thresh, 12.92 * im_in, 1.055 * (im_in**(1 / 2.4)) - 0.055)
    return im_out
