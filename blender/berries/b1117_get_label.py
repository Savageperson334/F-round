# get_label
#
# Copied verbatim from https://github.com/axcelerateai/urdu-handwriting-recognition-using-deep-learning
#   file models/helpers.py, line 84
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_label(i):
    if i % 2 == 0:
        return "weights"
    else:
        return "biases"
