# format_dec
#
# Copied verbatim from https://github.com/tjyank/orrery-tui
#   file orrery/stellar/coords.py, line 74
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def format_dec(deg: float) -> str:
    sign = "−" if deg < 0 else "+"
    a = abs(deg)
    return f"{sign}{int(a):02d}°{int(a * 60 % 60):02d}′"
