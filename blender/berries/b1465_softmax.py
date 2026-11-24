# softmax
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/vector/__init__.py, line 3008
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from collections import defaultdict
from math import exp


def softmax(p):
    """ Returns a dict with float values that sum to 1.0
        (using generalized logistic regression).
    """
    if p:
        v = list(p.values())
        m = max(v)
        e = list([exp(x - m) for x in v]) # prevent overflow
        s = sum(e)
        v = list([x / s for x in e])
        p = defaultdict(float, list(zip(list(p.keys()), v)))
    return p
