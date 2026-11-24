# kind_of
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file book_chapters/brains.py, line 28
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def kind_of(births_per_100: float) -> str:
    """The kinds of world a changeless world falls into, by its births per 100 agents per iteration."""
    if births_per_100 == 0:
        return "frozen"
    if births_per_100 < 0.5:
        return "nearly frozen"
    if births_per_100 > 50:
        return "teeming"
    return "breeding"
