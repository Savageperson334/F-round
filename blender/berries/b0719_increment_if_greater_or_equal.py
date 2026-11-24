# increment_if_greater_or_equal
#
# Copied verbatim from https://github.com/SublimeText/Origami
#   file origami.py, line 11
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Origami, folds and paper
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def increment_if_greater_or_equal(x, threshold):
    if x >= threshold:
        return x + 1
    return x
