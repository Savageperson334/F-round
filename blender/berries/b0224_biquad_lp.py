# biquad_lp
#
# Copied verbatim from https://github.com/FartyPants/fm1-nachtfahrt
#   file tools/water_fit.py, line 32
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np

SR = 44100


def biquad_lp(fc, q):
    w = 2 * np.pi * fc / SR; a = np.sin(w) / (2 * q); c = np.cos(w)
    b = np.array([(1 - c) / 2, 1 - c, (1 - c) / 2]); aa = np.array([1 + a, -2 * c, 1 - a]); return b / aa[0], aa / aa[0]
