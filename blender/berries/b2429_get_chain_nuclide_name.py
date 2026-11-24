# get_chain_nuclide_name
#
# Copied verbatim from https://github.com/jlanversin/ONIX
#   file onix/nax/functions.py, line 507
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_chain_nuclide_name(chain, index):

    data = chain[index]
    name = data[0]

    return name
