# loop
#
# Copied verbatim from https://github.com/f0k/birdclef2018
#   file experiments/augment.py, line 16
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def loop(array, length):
    """
    Loops a given `array` along its first axis to reach a length of `length`.
    """
    if len(array) < length:
        array = np.asanyarray(array)
        if len(array) == 0:
            return np.zeros((length,) + array.shape[1:], dtype=array.dtype)
        factor = length // len(array)
        if factor > 1:
            array = np.tile(array, (factor,) + (1,) * (array.ndim - 1))
        missing = length - len(array)
        if missing:
            array = np.concatenate((array, array[:missing:]))
    return array
