# hsl_to_rgbnorm
#
# Copied verbatim from https://github.com/PaulKlinger/satellite_tracker
#   file demo.py, line 109
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def hsl_to_rgbnorm(h, s, l):
    # 0<=h<=360
    # 0<s<1
    # 0<l<1
    c = (1 - np.abs(2 * l - 1)) * s
    hp = h / 60
    x = c * (1 - np.abs(hp % 2 - 1))
    r1, g1, b1 = (c, x, 0) if 0 <= hp <= 1 else (x, c, 0) if 1 <= hp <= 2 else (0, c, x) if 2 <= hp <= 3 else \
        (0, x, c) if 3 <= hp <= 4 else (x, 0, c) if 4 <= hp <= 5 else (c, 0, x)
    m = l - c / 2
    return (r1 + m, g1 + m, b1 + m)
