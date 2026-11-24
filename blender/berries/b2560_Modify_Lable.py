# Modify_Lable
#
# Copied verbatim from https://github.com/liaochengcsu/BCE-Net
#   file utils/seg_metric.py, line 95
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Historic cartography
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def Modify_Lable(Mask,GT):
    error = np.abs(GT-Mask)
    error[error > 0.85] = 1
    error[error <= 0.85] = 0
    return np.abs(GT-error)
