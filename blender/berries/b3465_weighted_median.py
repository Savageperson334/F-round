# weighted_median
#
# Copied verbatim from https://github.com/pyrocko/qseek
#   file src/qseek/utils.py, line 475
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def weighted_median(data: np.ndarray, weights: np.ndarray | None = None) -> float:
    """Calculate the weighted median of an array/list using numpy.

    Parameters:
        data (np.ndarray): The input array/list.
        weights (np.ndarray | None): The weights corresponding to each
            element in the data array/list.
            If None, the function calculates the regular median.

    Returns:
        float: The weighted median.

    Raises:
        TypeError: If the data and weights arrays/lists cannot be sorted together.
    """
    if weights is None:
        return float(np.median(data))

    if weights.sum() == 0.0:
        raise ValueError("weights sum to zero, can't normalize")

    data = np.atleast_1d(data.squeeze())
    weights = np.atleast_1d(weights.squeeze())

    sorted_indices = np.argsort(data)
    s_data = data[sorted_indices]
    s_weights = weights[sorted_indices]

    midpoint = 0.5 * s_weights.sum()
    if np.any(weights > midpoint):
        w_median = (data[weights == weights.max()])[0]
    else:
        cs_weights = np.cumsum(s_weights)
        idx = np.where(cs_weights <= midpoint)[0][-1]
        if cs_weights[idx] == midpoint:
            w_median = np.mean(s_data[idx : idx + 2])
        else:
            w_median = s_data[idx + 1]
    return float(w_median)
