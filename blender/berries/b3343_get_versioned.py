# get_versioned
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/io/ims.py, line 485
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_versioned(x, version_dialect):
    if isinstance(x, dict):
        for v in (tuple(version_dialect), version_dialect[0], None):
            if v in x:
                return x[v]
    else:
        return x
