# step_4
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/vector/stemmer.py, line 251
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

suffixes4 = [
    ("al", ("al",)),
    ("ce", ("ance", "ence")),
    ("er", ("er",)),
    ("ic", ("ic",)),
    ("le", ("able", "ible")),
    ("nt", ("ant", "ement", "ment", "ent")),
    ("e",  ("ate", "ive", "ize")),
    (("m", "i", "s"), ("ism", "iti", "ous"))
]

overstemmed = ("gener", "commun", "arsen")

RE_R1 = re.compile(r"[aeiouy][^aeiouy]")


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


def step_4(w):
    """ Step 4 strips -ant, -ent etc. suffixes.
        This only happens if there is more than one vowel-consonant pair before the suffix.
    """
    for suffix, rules in suffixes4:
        if w.endswith(suffix):
            for A in rules:
                if w.endswith(A):
                    return R2(w).endswith(A) and w[:-len(A)] or w
    if R2(w).endswith("ion") and w[:-3].endswith(("s", "t")):
        # Delete -ion if preceded by s or t.
        return w[:-3]
    return w
