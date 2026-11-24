# share_of
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file explain_minimal.py, line 119
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def share_of(a: float, b: float) -> float:
    """Two outputs read as a fraction between 0 and 1: a negative one counts as nothing."""
    a, b = max(0.0, a), max(0.0, b)
    total = a + b
    return (a / total) if total > 0 else 0.5
