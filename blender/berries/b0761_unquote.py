# unquote
#
# Copied verbatim from https://github.com/Worldwave/Wakes
#   file tools/host-tests/mkovr.py, line 15
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def unquote(s):
    # CMake's own unescaping for a quoted argument, in ONE pass: \n \t \" \\.
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c == '\\' and i + 1 < len(s):
            nxt = s[i + 1]
            out.append({'n': '\n', 't': '\t', 'r': '\r'}.get(nxt, nxt))
            i += 2
        else:
            out.append(c)
            i += 1
    return ''.join(out)
