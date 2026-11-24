# get_combine_indexes
#
# Copied verbatim from https://github.com/jlanversin/ONIX
#   file onix/nax/functions.py, line 1117
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_combine_indexes(index_list1, index_list2):

    combined_indexes = list(set(index_list1+index_list2))
    combined_indexes.sort()

    return combined_indexes
