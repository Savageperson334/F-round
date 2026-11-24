# make_chunks
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/gui/snuffler/pile_viewer.py, line 103
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from itertools import groupby
import operator


def make_chunks(items):
    '''
    Split a list of integers into sublists of consecutive elements.
    '''
    return [list(map(operator.itemgetter(1), g)) for k, g in groupby(
        enumerate(items), (lambda x: x[1]-x[0]))]
