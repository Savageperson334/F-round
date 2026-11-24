# nonetoempty
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/io/sac.py, line 35
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def nonetoempty(s):
    if s is None:
        return ''
    else:
        return s.strip()
