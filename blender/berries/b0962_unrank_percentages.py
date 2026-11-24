# unrank_percentages
#
# Copied verbatim from https://github.com/alepersichetti/WyrmHex
#   file wyrmhex.py, line 1134
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Cave surveys and subterranean maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def unrank_percentages(rank, count, total=100):
    """rank_percentages backwards: the list of `count` numbers at that place."""
    values, left = [], total
    for i in range(count):
        after = count - i - 1
        value = 0
        while rank >= math.comb(left - value + after, after):
            rank -= math.comb(left - value + after, after)
            value += 1
        values.append(value)
        left -= value
    return values
