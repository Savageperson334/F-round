# collapse_linebreaks
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/web/__init__.py, line 1059
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def collapse_linebreaks(string, threshold=1):
    """ Returns a string with consecutive linebreaks collapsed to at most the given threshold.
        Whitespace on empty lines and at the end of each line is removed.
    """
    n = "\n" * threshold
    p = [s.rstrip() for s in string.splitlines()]
    string = "\n".join(p)
    string = re.sub(n + r"+", n, string)
    return string
