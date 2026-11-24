# uniq
#
# Copied verbatim from https://github.com/bluetomlee/NetEase-MusicBox
#   file src/api.py, line 15
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Mechanical music boxes and organs
#   the same function also appears in: wzpan/MusicBoxApi
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def uniq(arr):
    arr2 = list(set(arr))
    arr2.sort(key=arr.index)
    return arr2
