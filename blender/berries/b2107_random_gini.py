# random_gini
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file research/screen/health.py, line 238
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def random_gini(mean: float) -> float:
    """The Gini of whole tokens dealt out at random, one at least, at a mean of `mean` an agent (geometric)."""
    return (mean - 1.0) / (2.0 * mean - 1.0) if mean > 1.0 else 0.0
