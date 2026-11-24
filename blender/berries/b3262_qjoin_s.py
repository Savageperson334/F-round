# qjoin_s
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/util.py, line 2942
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

g_re_escape_s = re.compile(r'([\\\'])')

g_re_qsplit_sep = {}

g_re_trivial = re.compile(r'\A[^\'"\s]+\Z')

g_re_trivial_sep = {}


def escape_s(s):
    '''
    Backslash-escape single-quotes and backslashes.

    Example: ``Jack's`` => ``Jack\\'s``

    '''
    return g_re_escape_s.sub(r'\\\1', s)


def get_re_trivial(sep):
    if sep is None:
        return g_re_trivial
    else:
        if sep not in g_re_qsplit_sep:
            assert len(sep) == 1
            assert sep not in '\'"'
            esep = re.escape(sep)
            g_re_trivial_sep[sep] = re.compile(r'\A[^\'"' + esep + r']+\Z')

        return g_re_trivial_sep[sep]


def qjoin_s(it, sep=None):
    '''
    Join sequence of strings into a line, single-quoting non-trivial strings.

    Example:  ``["55", "Sparrow's Island"]`` => ``"55 'Sparrow\\\\'s Island'"``
    '''
    re_trivial = get_re_trivial(sep)

    if sep is None:
        sep = ' '

    return sep.join(
        w if re_trivial.search(w) else "'%s'" % escape_s(w) for w in it)
