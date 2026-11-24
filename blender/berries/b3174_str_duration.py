# str_duration
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/guts.py, line 1531
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

duration_unit_factors = dict(
    s=1.0,
    m=60.0,
    h=3600.0,
    d=24*3600.0,
    y=365*24*3600.0)


def str_duration(d):
    for k in 'ydhms':
        if abs(d) >= duration_unit_factors[k]:
            return '%g' % (d / duration_unit_factors[k]) + k

    return '%g' % d
