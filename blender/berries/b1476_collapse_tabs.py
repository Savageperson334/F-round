# collapse_tabs
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/web/__init__.py, line 1047
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

RE_TABS = re.compile(r"\t+", re.M)


def collapse_tabs(string, indentation=False, replace=" "):
    """ Returns a string with (consecutive) tabs replaced by a single space.
        Whitespace on empty lines and at the end of each line is removed.
        With indentation=True, retains leading whitespace on each line.
    """
    p = []
    for x in string.splitlines():
        n = indentation and len(x) - len(x.lstrip()) or 0
        p.append(x[:n] + RE_TABS.sub(replace, x[n:]).strip())
    return "\n".join(p)
