# combine_selections
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/squirrel/client/fdsn.py, line 95
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def combine_selections(selection):
    out = []
    last = None
    for this in selection:
        if last and this[:4] == last[:4] and this[4] == last[5]:
            last = last[:5] + (this[5],)
        else:
            if last:
                out.append(last)

            last = this

    if last:
        out.append(last)

    return out
