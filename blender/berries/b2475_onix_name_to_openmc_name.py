# onix_name_to_openmc_name
#
# Copied verbatim from https://github.com/jlanversin/ONIX
#   file onix/utils/functions.py, line 619
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def onix_name_to_openmc_name(name):

    """Converts a nuclide's name written with ONIX format ('U-235*') into OpenMC format ('U235_m1').

    **Note**: ONIX will adopt OpenMC name format in the next release.

    Parameters
    ----------
    name: str
        Name of a nuclide in ONIX format ('U-235*')
    """
    openmc_name = name.replace('-', '')
    openmc_name = openmc_name.replace('*','_m1')

    return openmc_name
