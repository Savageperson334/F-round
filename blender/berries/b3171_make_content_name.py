# make_content_name
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/guts.py, line 214
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def make_content_name(name):
    if name.endswith('_list'):
        return name[:-5]
    elif name.endswith('s'):
        return name[:-1]
    else:
        return name
