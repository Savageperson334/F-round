# find_vowel
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/vector/stemmer.py, line 102
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

VOWELS = ["a", "e", "i", "o", "u", "y"]


def find_vowel(w):
    """ Returns the index of the first vowel in the word.
        When no vowel is found, returns len(word).
    """
    for i, ch in enumerate(w):
        if ch in VOWELS:
            return i
    return len(w)
