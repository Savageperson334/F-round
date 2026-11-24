# str_charset_to_lists
#
# Copied verbatim from https://github.com/byuawsfhtl/HandwritingRecognition
#   file hwr/dataset.py, line 18
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def str_charset_to_lists(charset):
    """
    Turns string containing all desired characters into list of chars and indices. This is required for mapping
    between integer and char representations for use in the recognition model.

    :param charset: charset as string of chars to be represented in model.
    """
    chars = list(charset)
    indices = list(range(1, len(chars) + 1))
    return chars, indices
