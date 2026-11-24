# lerp
#
# Copied verbatim from https://github.com/LingDong-/ttf2hershey
#   file truetype/glyphcurves.py, line 6
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Generative typography and glyphs
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def lerp(p0,p1,t):
    x = (1-t) * p0[0] + t * p1[0]
    y = (1-t) * p0[1] + t * p1[1]
    return [x,y]
