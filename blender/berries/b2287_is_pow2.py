# is_pow2
#
# Copied verbatim from https://github.com/interactive-sonification/pya
#   file pya/helper/helpers.py, line 184
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sound sonification
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def is_pow2(val):
    """Check if input is a power of 2 return a bool result."""
    return False if val <= 0 else math.log(val, 2).is_integer()
