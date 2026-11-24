# upper_consonant_y
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/vector/stemmer.py, line 332
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

VOWELS = ["a", "e", "i", "o", "u", "y"]


def upper_consonant_y(w):
    """ Sets the initial y, or y after a vowel, to Y.
        Of course, y is interpreted as a vowel and Y as a consonant.
    """
    a = []
    p = None
    for ch in w:
        if ch == "y" and (p is None or p in VOWELS):
            a.append("Y")
        else:
            a.append(ch)
        p = ch
    return "".join(a)
