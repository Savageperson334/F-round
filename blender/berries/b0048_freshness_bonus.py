# freshness_bonus
#
# Copied verbatim from https://github.com/Anko3o/Orrery
#   file strength/strength.py, line 161
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

FRESHNESS_AMPLITUDE = 1.0

FRESHNESS_HALF_LIFE_HRS = 36.0


def freshness_bonus(days: float) -> float:
    """刚存进来的记忆有一阵「印象很新」：×2 起步，三天后归 1。"""
    return 1.0 + FRESHNESS_AMPLITUDE * math.exp(-(days * 24.0) / FRESHNESS_HALF_LIFE_HRS)
