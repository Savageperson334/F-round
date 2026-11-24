# neighborhood_density
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/weeding.py, line 14
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def neighborhood_density(dists, neighborhood=1):
    sdists = dists.copy()
    sdists.sort(axis=1)
    meandists = num.mean(sdists[:, 1:1+neighborhood], axis=1)
    return meandists
