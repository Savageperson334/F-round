# trail_span_days
#
# Copied verbatim from https://github.com/tjyank/orrery-tui
#   file orrery/trails.py, line 19
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

MAX_TRAIL_DAYS = 3 * 365.25

TRAIL_REAL_SECONDS = 15.0


def trail_span_days(rate: float) -> float:
    """Signed: negative when time runs forward, so the trail reaches back into the past."""
    span = min(abs(rate) * TRAIL_REAL_SECONDS / 86400.0, MAX_TRAIL_DAYS)
    return -span if rate >= 0 else span
