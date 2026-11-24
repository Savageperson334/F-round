# format_ra
#
# Copied verbatim from https://github.com/tjyank/orrery-tui
#   file orrery/stellar/coords.py, line 67
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def format_ra(deg: float) -> str:
    h = deg / 15
    hh, mm = int(h), int(h * 60 % 60)
    ss = h * 3600 % 60
    return f"{hh:02d}h{mm:02d}m{ss:02.0f}s"
