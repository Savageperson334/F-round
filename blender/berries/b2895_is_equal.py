# is_equal
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/helper.py, line 636
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def is_equal(a, b, rel_precision=1e-5):
    if (a + b) != 0:
        if ((0.5 * abs(a - b) / (abs(a + b))) < rel_precision):
            return True
        else:
            return False
    else:
        if a == 0:
            return True
        else:
            if ((0.5 * abs(a - b) / (abs(a) + abs(b))) < rel_precision):
                return True
            else:
                return False
