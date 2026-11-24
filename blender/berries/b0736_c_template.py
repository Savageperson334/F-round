# c_template
#
# Copied verbatim from https://github.com/Worldwave/Wakes
#   file tools/gen_audio.py, line 34
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def c_template(name, text):
    """The file as a C string for the firmware to write to WAKES/CNFG/ when it is missing (#52).
    Non-ASCII as octal escapes (a hex escape would swallow the hex digits after it)."""
    out = ['#if defined(SP1_CNFG_TEMPLATES)', 'static const char %s[] =' % name]
    for ln in text.splitlines(keepends=True):
        lit = ''
        for b in ln.encode('utf-8'):
            ch = chr(b)
            if ch == '\\':
                lit += '\\\\'
            elif ch == '"':
                lit += '\\"'
            elif ch == '\n':
                lit += '\\n'
            elif ch == '\t':
                lit += '\\t'
            elif 0x20 <= b < 0x7f:
                lit += ch
            else:
                lit += '\\%03o' % b
        out.append('\t"%s"' % lit)
    out += ['\t;' if text else '\t"";', '#endif']
    return out
