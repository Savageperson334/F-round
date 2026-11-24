# get_xs_nucl
#
# Copied verbatim from https://github.com/jlanversin/ONIX
#   file onix/utils/functions.py, line 444
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_xs_nucl(xs_lib):
    """Gets the list of nuclides from a cross section dictionnary.

    Parameters
    ----------
    xs_lib: dict
        A cross section dictionnary
    """
    xs_nucl = []
    for zamid in xs_lib:
        xs_nucl.append(zamid)

    return xs_nucl
