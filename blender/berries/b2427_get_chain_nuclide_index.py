# get_chain_nuclide_index
#
# Copied verbatim from https://github.com/jlanversin/ONIX
#   file onix/nax/functions.py, line 489
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_chain_nuclide_index(chain, nuclide):

    index = 0
    for data in chain:
        if data[0] == nuclide:
            break
        index += 1

    return index
