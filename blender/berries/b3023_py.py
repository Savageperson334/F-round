# py
#
# Copied verbatim from https://github.com/oscillr/LRRY
#   file lrry/tools/import_owner_edits.py, line 298
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def py(v, ind=0):
    if isinstance(v, dict):
        return "{" + ", ".join("%r: %s" % (k, py(x)) for k, x in v.items()) + "}"
    return repr(v)
