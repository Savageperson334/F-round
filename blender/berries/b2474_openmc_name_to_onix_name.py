# openmc_name_to_onix_name
#
# Copied verbatim from https://github.com/jlanversin/ONIX
#   file onix/utils/functions.py, line 594
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def is_number(s):
    """Check whether s is a float.

    Parameters
    ----------
    s: NA
    """
    try:
        float(s)
        return True
    except ValueError:
        return False


def openmc_name_to_onix_name(name):

    """Converts a nuclide's name written with OpenMC format ('U235_m1') into ONIX format ('U-235*').

    **Note**: ONIX will adopt OpenMC name format in the next release.

    Parameters
    ----------
    name: str
        Name of a nuclide in OpenMC format ('U235_m1')
    """
    i = 0
    while not is_number(name[i]):
        i += 1

    am = name[i:]
    am = am.replace('_m1', '*')
    am = am.replace('m', '*') # used in jeff3.3
    am = am.replace('n', '*') # used in jeff3.3
    onix_name = name[:i] + '-' + am



    return onix_name
