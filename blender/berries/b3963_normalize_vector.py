# normalize_vector
#
# Copied verbatim from https://github.com/xaviermouy/ecosound
#   file ecosound/core/tools.py, line 131
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def normalize_vector(vec):
    """
    Normalize the amplitude of a 1-D vector.

    Removes the mean (DC offset) and scales the vector so that its maximum
    absolute value is 1.

    Parameters
    ----------
    vec : numpy.ndarray
        1-D array to normalize.

    Returns
    -------
    normVec : numpy.ndarray
        Mean-subtracted and amplitude-normalized version of ``vec``.

    """
    # vec = vec+abs(min(vec))
    # normVec = vec/max(vec)
    # normVec = (normVec - 0.5)*2
    vec = vec - np.mean(vec)
    normVec = vec / max(vec)
    return normVec
