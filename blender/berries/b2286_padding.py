# padding
#
# Copied verbatim from https://github.com/interactive-sonification/pya
#   file pya/helper/helpers.py, line 151
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sound sonification
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def padding(x, width, tail=True, constant_values=0):
    """Pad signal with certain width, support 1-3D tensors. 
    Use it to add silence to a signal
    TODO: CHECK pad array


    Parameters
    ----------
    x : np.ndarray
        A numpy array
    width : int
        The amount of padding. 
    tail : bool
        If true pad to the tail, else pad to the start.
    constant_values : int or float or None
        The value to be padded, add None will pad nan to the array

    Returns
    -------
    _ : np.ndarray
        Padded array
    """
    pad = (0, width) if tail else (width, 0)
    if x.ndim == 1:
        return np.pad(x, (pad), mode='constant', constant_values=constant_values)
    elif x.ndim == 2:
        return np.pad(x, (pad, (0, 0)), mode='constant', constant_values=constant_values)
    elif x.ndim == 3:
        return np.pad(x, ((0, 0), pad, (0, 0)), mode='constant', constant_values=constant_values)
    else:
        raise AttributeError("only support ndim 1 or 2, 3. For higher please just use np.pad ")
