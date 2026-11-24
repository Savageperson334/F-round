# moments
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file book_chapters/space.py, line 23
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def moments(last: int) -> tuple:
    """Five moments of a world's settled life, a sixth of its life apart, the last its last iteration."""
    step = (last + 1) // 6
    return (2 * step, 3 * step, 4 * step, 5 * step, last)
