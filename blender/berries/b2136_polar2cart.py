# polar2cart
#
# Copied verbatim from https://github.com/guaix-ucm/megara-tools
#   file megaratools/atan_model.py, line 368
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def polar2cart(r, theta):
    y = r * np.cos(theta)  # # referenced to vertical
    x = r * np.sin(theta)
    return x, y
