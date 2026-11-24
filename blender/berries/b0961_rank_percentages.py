# rank_percentages
#
# Copied verbatim from https://github.com/alepersichetti/WyrmHex
#   file wyrmhex.py, line 1120
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Cave surveys and subterranean maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def rank_percentages(values, total=100):
    """The position of a list of whole numbers adding up to `total` at most,
    among all such lists (counted in order); -1 if it isn't one."""
    if any(v != int(v) or v < 0 for v in values) or sum(values) > total:
        return -1
    rank, left = 0, total
    for i, value in enumerate(values):
        after = len(values) - i - 1
        # every list with a smaller value here comes first
        rank += sum(math.comb(left - v + after, after) for v in range(int(value)))
        left -= int(value)
    return rank
