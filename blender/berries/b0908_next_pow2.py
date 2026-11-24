# next_pow2
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/util/util.py, line 180
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def next_pow2(num):
    """
    Calculates the next nearest power of 2 to the input. Uses
      2**ceil( log2( num ) ).

    Args:
        num (number): The number to round to the next power if two.

    Returns:
        number. The next power of 2 closest to num.
    """

    return int(2**np.ceil(np.log2(num)))
