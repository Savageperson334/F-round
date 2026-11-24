# order_nuclide_per_a
#
# Copied verbatim from https://github.com/jlanversin/ONIX
#   file onix/utils/functions.py, line 710
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def order_nuclide_per_a(nucl_list):

    """Orders a list of nuclides' z-a-m ids according to their mass number (a).

    Parameters
    ----------
    nucl_list: List of str
        List of nuclides' z-a-m ids
    """
    changed = True
    while changed:
        changed = False
        for i in range(len(nucl_list) - 1):
            zamid0 = nucl_list[i]
            zamid1 = nucl_list[i+1]


            if zamid0 > zamid1:
                nucl_list[i], nucl_list[i+1] = nucl_list[i+1], nucl_list[i]
                changed = True

    return nucl_list
