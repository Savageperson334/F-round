# at_end
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file book_chapters/candidates.py, line 104
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

REPLAYED = {"K-reach-random-forced-s1": "B2-10000-e10e0d-s001", "Y-mix-keepone-s1": "B2-10000-82bd1e-s001"}


def at_end(name: str) -> str:
    """Where a long run is read at 10,000: the lab's run for a replayed one, else its pilot copy."""
    return REPLAYED.get(name, f"LC/{name}")
