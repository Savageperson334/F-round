# get_intervalls
#
# Copied verbatim from https://github.com/livingingroups/animal2vec
#   file get_results_for_single_manifest_split.py, line 185
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from itertools import groupby


def get_intervalls(data, shift=0):
    # Group the array in segments with itertools groupby function
    grouped = (list(g) for _, g in groupby(enumerate(data), lambda t: t[1]))
    # Only add the interval if it is with values larger than 0
    return [(g[0][0] + shift, min([len(data) - 1, g[-1][0] + shift])) for g in grouped if g[0][1] == 1]
