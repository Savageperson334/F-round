# split_text
#
# Copied verbatim from https://github.com/MZaFaRM/TheLifeOfPy
#   file src/helper.py, line 8
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def split_text(text, char_limit=42):
    """
    Splits the input text into lines with a maximum of `char_limit` characters per line.
    It ensures words are not cut off in the middle unless a single word exceeds the limit.

    :param text: The input string to be split.
    :param char_limit: The maximum number of characters per line.
    :return: A list of lines with the specified character limit.
    """
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        # If adding the word would exceed the limit, start a new line
        if (
            sum(len(w) for w in current_line) + len(current_line) + len(word)
            > char_limit
        ):
            lines.append(" ".join(current_line))
            current_line = [word]
        else:
            current_line.append(word)

    # Add the remaining words as the last line
    if current_line:
        lines.append(" ".join(current_line))

    return lines
