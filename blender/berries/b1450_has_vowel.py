# has_vowel
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/vector/stemmer.py, line 112
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

VOWELS = ["a", "e", "i", "o", "u", "y"]


def has_vowel(w):
    """ Returns True if there is a vowel in the given string.
    """
    for ch in w:
        if ch in VOWELS:
            return True
    return False
