# remove_adjancent_duplicates
#
# Copied verbatim from https://github.com/ScopeFoundry/ScopeFoundry
#   file logged_quantity/lq_intervaled_range.py, line 187
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def remove_adjancent_duplicates(ar: np.ndarray, tol: float = 0) -> np.ndarray:
    """
    Filters adjacent duplicates in a numpy array based on a tolerance.
    Returns the filtered array.
    """
    if len(ar) == 0:
        return ar
    mask = np.abs(np.diff(ar)) > tol
    mask = np.insert(mask, 0, True)  # Keep the first element
    return ar[mask]
