# split_top
#
# Copied verbatim from https://github.com/jbschooley/Virtual-FM-1
#   file engines/felucca/fel_state.py, line 46
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def split_top(s):
    """'a, {b, c}, d' -> ['a', '{b, c}', 'd'] (commas outside brackets and strings: c"a,b" is one)"""
    out, depth, cur, quoted = [], 0, '', False
    for c in s:
        if c == '"':   # (IR strings escape a quote as \22: none inside)
            quoted = not quoted
        elif quoted:
            pass
        elif c in '[{<(':
            depth += 1
        elif c in ']}>)':
            depth -= 1
        if c == ',' and depth == 0 and not quoted:
            out.append(cur.strip())
            cur = ''
        else:
            cur += c
    if cur.strip():
        out.append(cur.strip())
    return out
