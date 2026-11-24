# float_or_none
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/model/station.py, line 433
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def float_or_none(s):
    if s is None:
        return None
    elif isinstance(s, str) and s.lower() == 'nan':
        return None
    else:
        return float(s)
