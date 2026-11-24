# c_string
#
# Copied verbatim from https://github.com/Worldwave/Wakes
#   file tools/gen_logs.py, line 82
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def c_string(text):
    """The text as C string literals, one per line; non-ASCII as octal escapes (a hex escape
    would swallow the hex digits after it)."""
    out = []
    for ln in text.splitlines(keepends=True):
        s = ''
        for b in ln.encode('utf-8'):
            c = chr(b)
            if c == '\\':
                s += '\\\\'
            elif c == '"':
                s += '\\"'
            elif c == '\n':
                s += '\\n'
            elif c == '\t':
                s += '\\t'
            elif 0x20 <= b < 0x7f:
                s += c
            else:
                s += '\\%03o' % b
        out.append('\t"%s"' % s)
    return '\n'.join(out) if out else '\t""'
