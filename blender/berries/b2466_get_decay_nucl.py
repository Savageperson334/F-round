# get_decay_nucl
#
# Copied verbatim from https://github.com/jlanversin/ONIX
#   file onix/utils/functions.py, line 430
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_decay_nucl(decay_a_lib):
    """Gets the list of nuclides from a decay dictionnary.

    Parameters
    ----------
    decay_a_lib: dict
        A decay dictionnary
    """
    decay_nucl = []
    for zamid in decay_a_lib:
        decay_nucl.append(zamid)

    return decay_nucl
