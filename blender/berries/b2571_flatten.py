# flatten
#
# Copied verbatim from https://github.com/livingingroups/animal2vec
#   file animal2vec_inference.py, line 652
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def flatten(l):
    """helper function for flattening a list of lists"""
    return [item for sublist in l for item in sublist]
