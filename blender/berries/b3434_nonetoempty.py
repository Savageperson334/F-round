# nonetoempty
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/squirrel/io/backends/sac.py, line 39
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def nonetoempty(x):
    if x is None:
        return ''
    else:
        return x.strip()
