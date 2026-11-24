# strip_between
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/web/__init__.py, line 964
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def strip_between(a, b, string):
    """ Removes anything between (and including) string a and b inside the given string.
    """
    p = "%s.*?%s" % (a, b)
    p = re.compile(p, re.DOTALL | re.I)
    return re.sub(p, "", string)
