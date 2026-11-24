# is_name
#
# Copied verbatim from https://github.com/jlanversin/ONIX
#   file onix/utils/functions.py, line 123
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def is_name(string):

    """Check whether a string is a nuclide's name.

    Parameters
    ----------
    string: str
    """

    if '-' in string:
        return True
    else:
        return False
