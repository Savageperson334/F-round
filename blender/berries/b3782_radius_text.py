# radius_text
#
# Copied verbatim from https://github.com/tjyank/orrery-tui
#   file orrery/panels.py, line 19
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def radius_text(km: float) -> str:
    if km <= 0:
        return "unknown"  # Horizons doesn't know every small body's size
    if km < 1:
        return f"{km * 1000:,.0f} m"
    return f"{km:,.1f} km" if km < 100 else f"{km:,.0f} km"
