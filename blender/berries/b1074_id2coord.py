# id2coord
#
# Copied verbatim from https://github.com/anopara/multi-resolution-texture-synthesis
#   file multiResolution_textureSynthesis.py, line 204
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Textures and materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import floor


def id2coord(coordFlat, imgSize):
    row = floor(coordFlat / imgSize[1])
    col = coordFlat - row * imgSize[1]

    return [row, col]
