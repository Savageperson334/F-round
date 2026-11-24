# census_frame
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file research/screen/braintree.py, line 599
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def census_frame(at: int) -> int:
    """The frame of the agents alive at the start of iteration `at`: after the game before it (-1: the founders)."""
    return 2 * at - 1
