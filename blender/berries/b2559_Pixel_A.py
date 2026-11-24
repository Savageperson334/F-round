# Pixel_A
#
# Copied verbatim from https://github.com/liaochengcsu/BCE-Net
#   file utils/seg_metric.py, line 74
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Historic cartography
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def Pixel_A(Mask,GT):
    tp = np.sum(np.logical_and(Mask == 1, GT == 1))
    fp = np.sum(np.logical_and(Mask == 1, GT != 1))
    # tn = np.sum(np.logical_and(Mask != 1, GT != 1))
    fn = np.sum(np.logical_and(Mask != 1, GT == 1))
    return tp, fp, fn
