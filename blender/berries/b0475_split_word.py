# split_word
#
# Copied verbatim from https://github.com/MZaFaRM/TheLifeOfPy
#   file src/helper.py, line 240
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def split_word(text, max_size):
    """
    Splits a word into smaller parts if it exceeds the maximum size.

    :param text: The input string to be split.
    :param max_size: The maximum number of characters allowed.
    :return: A list of strings, each within the specified size limit.
    """
    if len(text) <= max_size:
        return [text]

    return [text[i : i + max_size] for i in range(0, len(text), max_size)]
