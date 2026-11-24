# coin
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file book_chapters/rounderas.py, line 157
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import comb


def coin(k: int, n: int) -> float:
    """Two-sided p of k or more heads, or as few, in n tosses of a fair coin."""
    tail = sum(comb(n, j) for j in range(max(k, n - k), n + 1)) / 2 ** n
    return min(1.0, 2 * tail)
