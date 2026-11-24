# step_2
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/vector/stemmer.py, line 206
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

VALID_LI = ["b", "c", "d", "e", "g", "h", "k", "m", "n", "r", "t"]

suffixes2 = [
    ("al", (("ational", "ate"), ("tional", "tion"))),
    ("ci", (("enci", "ence"), ("anci", "ance"))),
    ("er", (("izer", "ize"),)),
    ("li", (("bli", "ble"), ("alli", "al"), ("entli", "ent"), ("eli", "e"), ("ousli", "ous"))),
    ("on", (("ization", "ize"), ("isation", "ize"), ("ation", "ate"))),
    ("or", (("ator", "ate"),)),
    ("ss", (("iveness", "ive"), ("fulness", "ful"), ("ousness", "ous"))),
    ("sm", (("alism", "al"),)),
    ("ti", (("aliti", "al"), ("iviti", "ive"), ("biliti", "ble"))),
    ("gi", (("logi", "log"),))
]

RE_R1 = re.compile(r"[aeiouy][^aeiouy]")


def R1(w):
    """ R1 is the region after the first non-vowel following a vowel, 
        or the end of the word if there is no such non-vowel. 
    """
    m = RE_R1.search(w)
    if m:
        return w[m.end():]
    return ""


def step_2(w):
    """ Step 2 replaces double suffixes (singularization => singularize).
        This only happens if there is at least one vowel-consonant pair before the suffix.
    """
    for suffix, rules in suffixes2:
        if w.endswith(suffix):
            for A, B in rules:
                if w.endswith(A):
                    return R1(w).endswith(A) and w[:-len(A)] + B or w
    if w.endswith("li") and R1(w)[-3:-2] in VALID_LI:
        # Delete -li if preceded by a valid li-ending.
        return w[:-2]
    return w
