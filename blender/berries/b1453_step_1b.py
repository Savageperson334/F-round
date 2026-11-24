# step_1b
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/vector/stemmer.py, line 155
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

RE_R1 = re.compile(r"[aeiouy][^aeiouy]")

VOWELS = ["a", "e", "i", "o", "u", "y"]

DOUBLE = ["bb", "dd", "ff", "gg", "mm", "nn", "pp", "rr", "tt"]


def R1(w):
    """ R1 is the region after the first non-vowel following a vowel, 
        or the end of the word if there is no such non-vowel. 
    """
    m = RE_R1.search(w)
    if m:
        return w[m.end():]
    return ""


def has_vowel(w):
    """ Returns True if there is a vowel in the given string.
    """
    for ch in w:
        if ch in VOWELS:
            return True
    return False


def is_double_consonant(s):
    return s in DOUBLE


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


def is_short(w):
    """ A word is called short if it consists of a short syllable preceded by zero or more consonants. 
    """
    return is_short_syllable(w[-3:]) and len([ch for ch in w[:-3] if ch in VOWELS]) == 0


def step_1b(w):
    """ Step 1b handles -ed and -ing suffixes (or -edly and -ingly).
        Removes double consonants at the end of the stem and adds -e to some words.
    """
    if w.endswith("y") and w.endswith(("edly", "ingly")):
        w = w[:-2] # Strip -ly for next step.
    if w.endswith(("ed", "ing")):
        if w.endswith("ied"):
            # See -ies in step 1a.
            return len(w) == 4 and w[:-1] or w[:-2]
        if w.endswith("eed"):
            # Replace by -ee if preceded by at least one vowel-consonant pair.
            return R1(w).endswith("eed") and w[:-1] or w
        for suffix in ("ed", "ing"):
            # Delete if the preceding word part contains a vowel.
            # - If the word ends -at, -bl or -iz add -e (luxuriat => luxuriate).
            # - If the word ends with a double remove the last letter (hopp => hop).
            # - If the word is short, add e (hop => hope).
            if w.endswith(suffix) and has_vowel(w[:-len(suffix)]):
                w = w[:-len(suffix)]
                if w.endswith(("at", "bl", "iz")):
                    return w + "e"
                if is_double_consonant(w[-2:]):
                    return w[:-1]
                if is_short(w):
                    return w + "e"
    return w
