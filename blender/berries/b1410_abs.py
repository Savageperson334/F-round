# abs
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/db/__init__.py, line 1274
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

sql_functions = \
    "first|last|count|min|max|sum|avg|stdev|group_concat|concatenate|" \
    "year|month|day|hour|minute|second|" \
    "length|lower|upper|substr|substring|replace|trim|round|random|rand|" \
    "strftime|date_format"


def abs(table, field):
    """ For a given <fieldname>, returns the absolute <tablename>.<fieldname>.
        This is useful when constructing queries with relations to other tables.
    """
    def _format(s):
        if "." not in s:
            # Field could be wrapped in a function: year(date) => year(table.date).
            p = s.endswith(")") and re.match(r"^(" + sql_functions + r")\(", s, re.I) or None
            i = p and len(p.group(0)) or 0
            return "%s%s.%s" % (s[:i], table, s[i:])
        return s
    if isinstance(field, (list, tuple)):
        return [_format(f) for f in field]
    return _format(field)
