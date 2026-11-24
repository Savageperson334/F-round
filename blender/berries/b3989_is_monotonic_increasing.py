# is_monotonic_increasing
#
# Copied verbatim from https://github.com/xdas-dev/xdas
#   file xdas/coordinates/core.py, line 1780
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def is_monotonic_increasing(x):
    """Return ``True`` if every element of *x* is strictly greater than the previous one."""
    zero = np.timedelta64(0) if np.issubdtype(x.dtype, np.datetime64) else 0
    return np.all(np.diff(x) > zero)
