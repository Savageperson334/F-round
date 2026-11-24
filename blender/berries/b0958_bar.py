# bar
#
# Copied verbatim from https://github.com/alepersichetti/WyrmHex
#   file wyrmhex.py, line 924
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Cave surveys and subterranean maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def bar(fraction, cells):
    """Text progress bar, e.g. [███░░░], with cells squares filled up to fraction."""
    full = round(max(0.0, min(1.0, fraction)) * cells)
    return "[" + "█" * full + "░" * (cells - full) + "]"
