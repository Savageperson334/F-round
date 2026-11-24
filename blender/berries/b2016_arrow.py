# arrow
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file book_diagrams.py, line 78
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def arrow(x1: float, y1: float, x2: float, y2: float, cls: str = "dg-line") -> str:
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="{cls}" '
            f'marker-end="url(#dg-arrow)"/>')
