# finalize_construction
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/response.py, line 39
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def finalize_construction(breakpoints):
    breakpoints.sort()
    breakpoints_out = []
    f_last = None
    for f, c in breakpoints:
        if f_last is not None and f == f_last:
            breakpoints_out[-1][1] += c
        else:
            breakpoints_out.append([f, c])

        f_last = f

    breakpoints_out = [(f, c) for (f, c) in breakpoints_out if c != 0]
    return breakpoints_out
