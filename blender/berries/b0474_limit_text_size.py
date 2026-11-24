# limit_text_size
#
# Copied verbatim from https://github.com/MZaFaRM/TheLifeOfPy
#   file src/helper.py, line 226
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def limit_text_size(text, max_size):
    """
    Limits the size of the text to a maximum number of characters.
    If the text exceeds the limit, it truncates the text and adds ellipsis.

    :param text: The input string to be limited.
    :param max_size: The maximum number of characters allowed.
    :return: The limited string with ellipsis if truncated.
    """
    if len(text) > max_size:
        return text[: max_size - 1] + "."
    return text
