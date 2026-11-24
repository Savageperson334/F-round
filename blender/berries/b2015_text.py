# text
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file book_diagrams.py, line 67
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def text(x: float, y: float, s: str, cls: str = "dg-t", anchor: str = "start") -> str:
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    lead = len(s) - len(s.lstrip(" "))
    s = "\u00a0" * lead + s[lead:]
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" text-anchor="{anchor}">{s}</text>'
