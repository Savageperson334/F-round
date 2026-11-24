# part_of_list
#
# Copied verbatim from https://github.com/OPM/opm-geochemistry
#   file pyGeoChem/pyGeoChem/io_cpp_solver/util.py, line 144
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def part_of_list(list,elem):
    '''
    checks if elem contains any elements in list
    '''
    for li in list:
        if li in elem:
            return True
    return False
