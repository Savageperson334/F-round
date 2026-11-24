# repitch
#
# Copied verbatim from https://github.com/isod89/clipper-fm1
#   file tools/gen_hiphop_pack.py, line 100
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#   the same function also appears in: isod89/clipper-pro
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def repitch(x, sr, semis):
    """play x semis higher (faster) by interpolation, at sr"""
    if abs(semis) < 1e-4:
        return x
    r = 2 ** (semis / 12)
    t = np.arange(0, len(x) - 1, r)
    return np.interp(t, np.arange(len(x)), x)
