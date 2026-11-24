# hue_between
#
# Copied verbatim from https://github.com/touchbr/Graphite
#   file scripts/soften_colormap.py, line 283
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def hue_between(hue: float, start: float, end: float) -> bool:
    hue %= 360
    start %= 360
    end %= 360
    if start <= end:
        return start <= hue <= end
    return hue >= start or hue <= end
