# kept
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file research/oee/strategies/mobs.py, line 55
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def kept(tokens: int, share: float) -> int:
    """What an agent must leave on its own node (the engine's keep_home)."""
    return max(1, int(math.ceil(share * tokens))) if share > 0 else 0
