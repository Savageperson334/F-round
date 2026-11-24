# f1
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file book_svg.py, line 111
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def f1(v: float) -> str:
    """A coordinate, to a tenth of a pixel."""
    s = f"{v:.1f}"
    return s[:-2] if s.endswith(".0") else s
