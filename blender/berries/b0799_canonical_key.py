# canonical_key
#
# Copied verbatim from https://github.com/aconz2/blender-addon-origamify
#   file origami.py, line 47
#   licence (as GitHub reports it): Unlicense   see ../licenses/
#   catalogue shelf: Origami, folds and paper
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def canonical_key(face1, edge, face2):
    if face1 < face2:
        return (face1, edge, face2)
    return (face2, edge, face1)
