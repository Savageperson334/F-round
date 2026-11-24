# vowel_mix
#
# Copied verbatim from https://github.com/isod89/clipper-fm1
#   file tools/gen_clipper_sets.py, line 83
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#   the same function also appears in: isod89/clipper-pro
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def vowel_mix(t, dur):
    """weights of U, O, A over time: oo .. oh .. ah through the first third, then ah"""
    x = np.clip(t / (0.34 * dur), 0, 1)
    x = x * x * (3 - 2 * x)
    wu = np.clip(1 - 2 * x, 0, 1)
    wa = np.clip(2 * x - 1, 0, 1)
    wo = 1 - wu - wa
    return wu, wo, wa
