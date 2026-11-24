# castagna_vs_to_vp
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/cake.py, line 4306
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def castagna_vs_to_vp(vs):
    '''
    Calculate vp from vs using Castagna's relation.

    Castagna's relation (the mudrock line) is an empirical relation for vp/vs
    for siliciclastic rocks (i.e. sandstones and shales). [Castagna et al.,
    1985]

        vp = 1.16 * vs + 1360 [m/s]

    :param vs: S-wave velocity [m/s]
    :returns: P-wave velocity [m/s]
    '''

    return vs*1.16 + 1360.0
