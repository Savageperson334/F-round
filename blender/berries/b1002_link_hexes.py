# link_hexes
#
# Copied verbatim from https://github.com/alepersichetti/WyrmHex
#   file wyrmhex.py, line 5191
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Cave surveys and subterranean maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def link_hexes(text, placed):
    """{hex:32} in a place's text points to D4Caltrops' place 32: the map hex
    where it was placed, or nothing if it isn't on this map."""
    def swap(m):
        return f" ({placed[int(m.group(1))]})" if m.group(1).isdigit() and int(m.group(1)) in placed else ""
    return re.sub(r" ?\{hex:(\d+|\?)\}", swap, text)
