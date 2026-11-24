# badnesses_c_mean
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/weeding.py, line 87
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def badnesses_c_mean(badnesses_nslc):
    # convert stream badnesses to station badnesses by averaging
    badnesses_nsl = {}
    for nslc, b in badnesses_nslc.items():
        nsl = nslc[:3]
        badnesses_nsl.setdefault(nsl, []).append(b)

    for nsl in list(badnesses_nsl.keys()):
        this_station_badness = badnesses_nsl[nsl]
        badnesses_nsl[nsl] = sum(this_station_badness) \
            / len(this_station_badness)

    return badnesses_nsl
