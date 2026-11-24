# round_pixels
#
# Copied verbatim from https://github.com/ymatterlab/ycrystal
#   file src/ycrystal/core/aspect.py, line 52
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def round_pixels(value: float) -> int:
    """Round half up to a whole number of pixels (``2.5`` → 3, unlike ``round``)."""
    return int(math.floor(value + 0.5))
