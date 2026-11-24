# step_5a
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/vector/stemmer.py, line 266
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

RE_R1 = re.compile(r"[aeiouy][^aeiouy]")

overstemmed = ("gener", "commun", "arsen")

VOWELS = ["a", "e", "i", "o", "u", "y"]


def R1(w):
    """ R1 is the region after the first non-vowel following a vowel, 
        or the end of the word if there is no such non-vowel. 
    """
    m = RE_R1.search(w)
    if m:
        return w[m.end():]
    return ""


def R2(w):
    """ R2 is the region after the first non-vowel following a vowel in R1, 
        or the end of the word if there is no such non-vowel.
    """
    if w.startswith(tuple(overstemmed)):
        return R1(R1(R1(w)))
    return R1(R1(w))


def is_consonant(s):
    return s not in VOWELS


def is_vowel(s):
    return s in VOWELS


def is_short_syllable(w, before=None):
    """ A short syllable in a word is either:
        - a vowel followed by a non-vowel other than w, x or Y and preceded by a non-vowel
        - a vowel at the beginning of the word followed by a non-vowel. 
        Checks the three characters before the given index in the word (or entire word if None).
    """
    if before is not None:
        i = before < 0 and len(w) + before or before
        return is_short_syllable(w[max(0, i - 3):i])
    if len(w) == 3 and is_consonant(w[0]) and is_vowel(w[1]) and is_consonant(w[2]) and w[2] not in "wxY":
        return True
    if len(w) == 2 and is_vowel(w[0]) and is_consonant(w[1]):
        return True
    return False


def step_5a(w):
    """ Step 5a strips suffix -e if preceded by multiple vowel-consonant pairs,
        or one vowel-consonant pair that is not a short syllable.
    """
    if w.endswith("e"):
        if R2(w).endswith("e") or R1(w).endswith("e") and not is_short_syllable(w, before=-1):
            return w[:-1]
    return w
