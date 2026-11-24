# step_3
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/vector/stemmer.py, line 228
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

suffixes3 = [
    ("e", (("icate", "ic"), ("ative", ""), ("alize", "al"))),
    ("i", (("iciti", "ic"),)),
    ("l", (("ical", "ic"), ("ful", ""))),
    ("s", (("ness", ""),))
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


def step_3(w):
    """ Step 3 replaces -ic, -ful, -ness etc. suffixes.
        This only happens if there is at least one vowel-consonant pair before the suffix.
    """
    for suffix, rules in suffixes3:
        if w.endswith(suffix):
            for A, B in rules:
                if w.endswith(A):
                    return R1(w).endswith(A) and w[:-len(A)] + B or w
    return w
