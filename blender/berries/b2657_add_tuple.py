# add_tuple
#
# Copied verbatim from https://github.com/matsuren/crownconv360depth
#   file models/costvolume_regularization.py, line 65
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Origami, folds and paper
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def add_tuple(feat_tuple1, feat_tuple2):
    a = feat_tuple1[0] + feat_tuple2[0]
    b = feat_tuple1[1] + feat_tuple2[1]
    return a, b
