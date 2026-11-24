# deflood
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/text/__init__.py, line 319
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def deflood(s, n=3):
    """ Returns the string with no more than n repeated characters, e.g.,
        deflood("NIIIICE!!", n=1) => "Nice!"
        deflood("nice.....", n=3) => "nice..."
    """
    if n == 0:
        return s[0:0]
    return re.sub(r"((.)\2{%s,})" % (n - 1), lambda m: m.group(1)[0] * n, s)
