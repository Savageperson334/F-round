# py
#
# Copied verbatim from https://github.com/oscillr/LRRY
#   file lrry/tools/import_bank.py, line 214
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def py(v):
    if isinstance(v, tuple):
        return "(" + ", ".join(py(x) for x in v) + ")"
    return repr(v)
