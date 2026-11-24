# finite_float_array
#
# Copied verbatim from https://github.com/Augtumn/IsoLeadToolkit
#   file visualization/plotting/kde_common.py, line 51
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def finite_float_array(values) -> np.ndarray:
    """Finite values of *values* as a float array - the input every estimator expects."""
    arr = np.asarray(values, dtype=float)
    if arr.ndim == 0:
        arr = arr.reshape(1)
    return arr[np.isfinite(arr)]
