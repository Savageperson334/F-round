# fmt_ms
#
# Copied verbatim from https://github.com/mbeher2200/DarkHours
#   file scripts/bench_10cities.py, line 119
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def fmt_ms(v) -> str:
    if v is None:
        return "  —  "
    return f"{v:>6.1f}"
