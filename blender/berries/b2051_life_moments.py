# life_moments
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file book_chapters/space.py, line 364
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def life_moments(last: int) -> tuple:
    """Moments of a whole life, closer together early on, ending at its last iteration."""
    return tuple(t for t in (10, 25, 50, 100, 200, 300, 500, 750, 1000, 1500, 2000, 2500) if t < last) + (last,)
