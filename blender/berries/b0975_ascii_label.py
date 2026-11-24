# ascii_label
#
# Copied verbatim from https://github.com/alepersichetti/WyrmHex
#   file wyrmhex.py, line 2718
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Cave surveys and subterranean maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import unicodedata


def ascii_label(name):
    """For --ascii-only: è -> e, and anything else non-ASCII goes."""
    return unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
