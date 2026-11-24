# hex_centre
#
# Copied verbatim from https://github.com/alepersichetti/WyrmHex
#   file wyrmhex.py, line 2911
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Cave surveys and subterranean maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def hex_origin(c, r, k):
    """Odd columns sit half a hex lower."""
    return 3 * k * c, 2 * k * r + (k if c & 1 else 0)


def hex_centre(c, r, k):
    """The letter square in the middle of hex (c, r): where rivers pass."""
    x0, y0 = hex_origin(c, r, k)
    return x0 + 2 * k + 1, y0 + k + 1
