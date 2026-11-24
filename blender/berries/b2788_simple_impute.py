# simple_impute
#
# Copied verbatim from https://github.com/morganjwilliams/exploratory-geochemistry
#   notebook 03_Missing_Data.ipynb (its code cells joined in order; line 20 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def simple_impute(arr, method='mean', threshold=0.01, limits=[]):
    """
    """
    if method == 'mean':
        # Note this is not a compositional mean, which should be: inv_alr(np.nanmean(alr(arr), axis=0)); this would require 1 nan-free column
        replace_vals = np.nanmean(arr, axis=0)
    elif method == 'eps': # constant arbitrarily small value
        replace_vals = 2*np.finfo(float).eps * np.ones(arr.shape)
    elif method == 'threshold': # detection limits or some ratio of the minimum values
        if not len(limits):
            replace_vals = np.tile(np.nanmin(arr, axis=0), (arr.shape[0])).reshape(arr.shape)
        else:
            assert len(limits) == arr.shape[1]
            replace_vals = np.tile(np.array(limits), (arr.shape[0])).reshape(arr.shape)
    else:
        raise NotImplementedError

    return np.where(~np.isfinite(arr), replace_vals, arr)
