# find_in_list
#
# Copied verbatim from https://github.com/sphereman/ChemBlender_2_0
#   file read.py, line 51
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def find_in_list(num, lst):
    for index, sublist in enumerate(lst, start=1):
        if num in sublist:
            return index
    return 0
