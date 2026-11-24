# error_not_whole
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/utility.py, line 1374
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def error_not_whole(f, errstr=""):
    """
    Test if float is a whole number, if not raise Error.
    """
    if f.is_integer():
        return int(f)
    else:
        raise ValueError("%s : %f is not a whole number!" % (errstr, f))
