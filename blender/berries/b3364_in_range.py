# in_range
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/model/event.py, line 77
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def in_range(vmin, vmax, v):
    return (vmin is None or (v is not None and vmin <= v)) \
        and (vmax is None or (v is not None and vmax >= v))
