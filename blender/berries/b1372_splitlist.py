# splitlist
#
# Copied verbatim from https://github.com/citiesskylines-csur/CSUR
#   file core/csur.py, line 39
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def splitlist(arr, val):
    arr = arr.copy()
    splited = []
    while val in arr:
        splited.append(arr[:arr.index(val)])
        arr = arr[arr.index(val) + 1:]
    if arr:
        splited.append(arr)
    return splited
