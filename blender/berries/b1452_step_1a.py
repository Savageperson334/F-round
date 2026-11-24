# step_1a
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/vector/stemmer.py, line 136
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


def step_1a(w):
    """ Step 1a handles -s suffixes.
    """
    if w.endswith("s"):
        if w.endswith("sses"):
            return w[:-2]
        if w.endswith("ies"):
            # Replace by -ie if preceded by just one letter,
            # otherwise by -i (so ties => tie, cries => cri).
            return len(w) == 4 and w[:-1] or w[:-2]
        if w.endswith(("us", "ss")):
            return w
        if find_vowel(w) < len(w) - 2:
            # Delete -s if the preceding part contains a vowel not immediately before the -s
            # (so gas and this retain the -s, gaps and kiwis lose it).
            return w[:-1]
    return w
