# find_tp
#
# Copied verbatim from https://github.com/worm-portal/pychnosz
#   file pychnosz/core/diagram.py, line 2182
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Metrology, microscopes and geology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def find_tp(predominant: np.ndarray) -> np.ndarray:
    """
    Find triple points in a predominance diagram.

    This function identifies the approximate positions of triple points
    (where three phases meet) in a 2-D predominance diagram by locating
    cells with the greatest number of different neighboring values.

    Parameters
    ----------
    predominant : np.ndarray
        Matrix of integers from diagram() output indicating which species
        predominates at each point. Should be a 2-D array where each value
        represents a different species/phase.

    Returns
    -------
    np.ndarray
        Array of shape (n, 2) where n is the number of triple points found.
        Each row contains [row_index, col_index] of a triple point location.
        Indices are 1-based to match R behavior.

    Examples
    --------
    >>> from pychnosz import *
    >>> reset()
    >>> basis(["corundum", "quartz", "oxygen"])
    >>> species(["kyanite", "sillimanite", "andalusite"])
    >>> a = affinity(T=[200, 900, 99], P=[0, 9000, 101], exceed_Ttr=True)
    >>> d = diagram(a)
    >>> tp = find_tp(d['predominant'])
    >>> # Get T and P at the triple point
    >>> Ttp = a['vals'][0][tp[0, 1] - 1]  # -1 for 0-based indexing
    >>> Ptp = a['vals'][1][::-1][tp[0, 0] - 1]  # reversed and -1

    Notes
    -----
    This is a Python translation of the R function find.tp() from CHNOSZ.
    The R version returns 1-based indices, and this Python version does too
    for consistency. When using these indices to access Python arrays,
    remember to subtract 1.

    The function works by:
    1. Rearranging the matrix as done by diagram() for plotting
    2. For each position, examining a 3x3 neighborhood
    3. Counting the number of unique values in that neighborhood
    4. Returning positions with the maximum count (typically 3 or more)
    """
    # Rearrange the matrix in the same way that diagram() does for 2-D predominance diagrams
    # R code: x <- t(x[, ncol(x):1])
    # This means: first reverse columns, then transpose
    x = np.transpose(predominant[:, ::-1])

    # Get all positions with valid values (> 0)
    valid_positions = np.argwhere(x > 0)

    if len(valid_positions) == 0:
        return np.array([])

    # For each position, count unique values in 3x3 neighborhood
    counts = []
    for pos in valid_positions:
        row, col = pos

        # Define the range to look at (3x3 except at edges)
        r1 = max(row - 1, 0)
        r2 = min(row + 1, x.shape[0] - 1)
        c1 = max(col - 1, 0)
        c2 = min(col + 1, x.shape[1] - 1)

        # Extract the neighborhood
        neighborhood = x[r1:r2+1, c1:c2+1]

        # Count unique values
        n_unique = len(np.unique(neighborhood))
        counts.append(n_unique)

    counts = np.array(counts)

    # Find positions with the maximum count
    max_count = np.max(counts)
    max_positions = valid_positions[counts == max_count]

    # Convert to 1-based indexing (to match R)
    # Return as [row, col] with 1-based indices
    result = max_positions + 1

    return result
