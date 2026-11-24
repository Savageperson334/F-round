# num_of
#
# Copied verbatim from https://github.com/oscillr/LRRY
#   file lrry/tools/convert_twin.py, line 387
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

OLD_NAMES = {("TRIO", 4): ["LP", "BP", "HP", "NOT"]}


def num_of(ctx, eng, pid, val):
    if isinstance(val, str):
        names = OLD_NAMES.get((eng, pid - ctx.e0))
        return names.index(val) if names and val in names else 0
    return int(val)
