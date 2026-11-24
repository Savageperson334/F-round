# severity
#
# Copied verbatim from https://github.com/mbeher2200/DarkHours
#   file scripts/verify_moonwash_grid.py, line 59
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def severity(delta):
    if delta < 0.10:
        return "none"
    if delta < 0.50:
        return "minor"
    if delta < 1.50:
        return "moderate"
    return "severe"
