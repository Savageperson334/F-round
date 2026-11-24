# get_fy_nucl
#
# Copied verbatim from https://github.com/jlanversin/ONIX
#   file onix/utils/functions.py, line 458
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_fy_nucl(fy_lib):
    """Gets the list of fission products from a fission yield dictionnary.

    Parameters
    ----------
    fy_lib: dict
        A fission yield dictionnary
    """
    fy_nucl = []
    for zamid in fy_lib:
        fy_nucl.append(zamid)

    return fy_nucl
