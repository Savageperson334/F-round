# width_of
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file book_svg.py, line 99
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def width_of(text: str, size: float) -> float:
    """How wide a text is drawn: every character of a monospaced face is 0.6 em."""
    return len(text) * size * 0.6
