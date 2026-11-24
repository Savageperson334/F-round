# rounding_step
#
# Copied verbatim from https://github.com/alexbarakov/amsterdam-by-building
#   file pipeline/s02_attributes.py, line 37
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Historic cartography
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def rounding_step(y: int) -> int:
    for step in (100, 50, 25, 10):
        if y % step == 0:
            return step
    return 1
