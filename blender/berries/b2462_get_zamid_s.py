# get_zamid_s
#
# Copied verbatim from https://github.com/jlanversin/ONIX
#   file onix/utils/functions.py, line 259
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_zamid_s(zamid):

    """Gets the state of a nuclide from a its z-a-m id. 1 = first excited state, 0 = ground state.

    Parameters
    ----------
    zamid: str
        z-a-m id of a nuclide
    """
    s = int(zamid[-1])

    return s
