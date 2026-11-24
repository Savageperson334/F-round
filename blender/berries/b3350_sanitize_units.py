# sanitize_units
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/io/stationxml.py, line 80
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

units_fixes = {
    'R': 'RAD',
    'R/S': 'RAD/S',
    'R/S**2': 'RAD/S**2',
    'COUNTS': 'COUNT'}


def sanitize_units(s):
    s = s.upper()
    return units_fixes.get(s, s)
