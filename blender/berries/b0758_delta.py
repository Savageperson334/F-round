# delta
#
# Copied verbatim from https://github.com/Worldwave/Wakes
#   file tools/ci/size_report.py, line 55
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def delta(a, b):
    d = b - a
    return "0" if d == 0 else f"{d:+,}"
