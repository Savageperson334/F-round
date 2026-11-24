# sort_lists
#
# Copied verbatim from https://github.com/OPM/opm-geochemistry
#   file pyGeoChem/pyGeoChem/io_cpp_solver/util.py, line 168
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def sort_lists(list1,list2,reverse=False):
    '''
    sort list1 low to high and list2 correspondingly
    '''
    l2=[x for _, x in sorted(zip(list1, list2),reverse=reverse)]
    l1=sorted(list1,reverse=reverse)
    return l1,l2
