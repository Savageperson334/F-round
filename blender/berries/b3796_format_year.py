# format_year
#
# Copied verbatim from https://github.com/tjyank/orrery-tui
#   file orrery/stellar/motion.py, line 141
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def format_year(year: float) -> str:
    y = math.floor(year)  # 2026.9 is still 2026: rounding would show next year from July on
    return f"{y:,} CE" if y >= 1 else f"{1 - y:,} BCE"
