# normalized_resolution_spread
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/ffi/fault.py, line 2047
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def normalized_resolution_spread(resolution, nparams):
    """
    Get normalized resolution spread after Atzori et al. 2019

    Must be between 0 and 1. The closer to zero the better can the model
    parameters be resolved by the data.
    """
    return num.linalg.norm(resolution - num.eye(nparams)) / nparams
