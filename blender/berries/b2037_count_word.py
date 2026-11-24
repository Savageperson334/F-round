# count_word
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file book_chapters/common.py, line 160
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

_WORDS = ("no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten")


def count_word(n: int) -> str:
    """'four' for 4, '26' for 26: small counts in words, as the text writes them."""
    return _WORDS[n] if 0 <= n < len(_WORDS) else f"{n:,}"
