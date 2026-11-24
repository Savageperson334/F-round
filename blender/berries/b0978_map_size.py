# map_size
#
# Copied verbatim from https://github.com/alepersichetti/WyrmHex
#   file wyrmhex.py, line 2887
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Cave surveys and subterranean maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def map_size(cols, rows, k):
    """(width, height) in letters of a cols x rows map with hexes of size k."""
    return 3 * k * (cols - 1) + 4 * k + 1, 2 * k * rows + k + 1
