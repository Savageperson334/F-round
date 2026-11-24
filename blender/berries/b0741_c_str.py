# c_str
#
# Copied verbatim from https://github.com/Worldwave/Wakes
#   file tools/gen_engines.py, line 188
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def c_str(s):
    s = s.encode("ascii", "replace").decode("ascii")[:24]
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
