# decrement_if_greater
#
# Copied verbatim from https://github.com/SublimeText/Origami
#   file origami.py, line 17
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Origami, folds and paper
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def decrement_if_greater(x, threshold):
    if x > threshold:
        return x - 1
    return x
