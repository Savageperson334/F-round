# to_num
#
# Copied verbatim from https://github.com/Anko3o/Orrery
#   file orrery/orrery-export.py, line 182
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def to_num(v, default=0.0):
    try:
        return float(v)
    except (TypeError, ValueError):
        return default
