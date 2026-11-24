# expand_size
#
# Copied verbatim from https://github.com/MuSAELab/hunee-b
#   file beessl/upstream/m2d/m2d/models_mae.py, line 27
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Beehives and unusual agriculture
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def expand_size(sz):
    if isinstance(sz, int):
        return [sz, sz]
    return sz
