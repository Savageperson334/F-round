# nextval_indices
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/icosphere.py, line 157
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def nextval_indices(a):
    return num.concatenate(
        [[0], num.where(num.diff(a) != 0)[0] + 1])
