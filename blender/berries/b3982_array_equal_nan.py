# array_equal_nan
#
# Copied verbatim from https://github.com/xdas-dev/xdas
#   file xdas/coordinates/core.py, line 35
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def array_equal_nan(x, y):
    """Like :func:`numpy.array_equal` but treats NaNs as equal, when supported.

    ``equal_nan=True`` raises ``TypeError`` on dtypes numpy's ``isnan`` does
    not support (e.g. fixed-width string arrays); fall back to a plain
    comparison there.
    """
    try:
        return np.array_equal(x, y, equal_nan=True)
    except TypeError:
        return np.array_equal(x, y)
