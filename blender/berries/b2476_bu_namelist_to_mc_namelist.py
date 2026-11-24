# bu_namelist_to_mc_namelist
#
# Copied verbatim from https://github.com/jlanversin/ONIX
#   file onix/utils/functions.py, line 635
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


def bu_namelist_to_mc_namelist(name_list):

    """Converts a list of nuclides' names written with ONIX format ('U-235*') into OpenMC format ('U235_m1').

    **Note**: ONIX will adopt OpenMC name format in the next release.

    Parameters
    ----------
    name_list: List of str
        List of nuclides' names in ONIX format ('U-235*')
    """
    new_name_list = []
    for name in name_list:
        new_name = onix_name_to_openmc_name(name)
        new_name_list.append(new_name)

    return new_name_list
