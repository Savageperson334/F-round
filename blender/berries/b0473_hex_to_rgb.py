# hex_to_rgb
#
# Copied verbatim from https://github.com/MZaFaRM/TheLifeOfPy
#   file src/helper.py, line 207
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def hex_to_rgb(hex_color: str):
    hex_color = hex_color.lstrip("#")
    hex_color = hex_color.ljust(6, "0")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))
