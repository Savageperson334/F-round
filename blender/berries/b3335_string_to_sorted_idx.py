# string_to_sorted_idx
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/gui/sparrow/elements/table.py, line 47
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def string_to_sorted_idx(values):
    val_sort = num.sort(values, axis=-1, kind='mergesort')
    val_sort_unique = num.unique(val_sort)

    val_to_idx = dict([
        (val_sort_unique[i], i)
        for i in range(val_sort_unique.shape[0])])

    return num.array([val_to_idx[val] for val in values])
