# next_power_of_2
#
# Copied verbatim from https://github.com/glumpy/glumpy
#   file glumpy/graphics/collections/base_collection.py, line 14
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def next_power_of_2(n):
    """ Return next power of 2 greater than or equal to n """
    n -= 1  # greater than OR EQUAL TO n
    shift = 1
    while (n+1) & n:  # n+1 is not a power of 2 yet
        n |= n >> shift
        shift *= 2
    return max(4, n+1)
