# vowel_consonant_pairs
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/vector/stemmer.py, line 121
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

VOWELS = ["a", "e", "i", "o", "u", "y"]


def is_consonant(s):
    return s not in VOWELS


def is_vowel(s):
    return s in VOWELS


def vowel_consonant_pairs(w, max=None):
    """ Returns the number of consecutive vowel-consonant pairs in the word.
    """
    m = 0
    for i, ch in enumerate(w):
        if is_vowel(ch) and i < len(w) - 1 and is_consonant(w[i + 1]):
            m += 1
            # An optimisation to stop searching once we reach the amount of <vc> pairs we need.
            if m == max:
                break
    return m
