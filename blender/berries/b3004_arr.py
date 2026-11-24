# arr
#
# Copied verbatim from https://github.com/oscillr/LRRY
#   file lrry/tools/gen_loader_screen.py, line 72
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def arr(name, vals, per=16, typ="uint8_t"):
    s = "static const %s %s[%d] = {\n" % (typ, name, len(vals))
    for i in range(0, len(vals), per):
        s += "    " + ",".join(str(v) for v in vals[i:i + per]) + ",\n"
    return s + "};\n"
