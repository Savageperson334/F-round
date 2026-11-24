# head
#
# Copied verbatim from https://github.com/FartyPants/fm1-nachtfahrt
#   file tools/water_fit.py, line 88
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def head(src, n, start, rate):
    pos = start + np.arange(n) * rate
    pos = pos % len(src)
    i = pos.astype(int); fr_ = pos - i
    return src[i] * (1 - fr_) + src[(i + 1) % len(src)] * fr_
