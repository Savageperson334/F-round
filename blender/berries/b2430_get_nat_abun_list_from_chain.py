# get_nat_abun_list_from_chain
#
# Copied verbatim from https://github.com/jlanversin/ONIX
#   file onix/nax/functions.py, line 514
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_nat_abun_list_from_chain(chain):

    nat_abun_list = []
    for data in chain:
        nat_abun_list.append(data[1])

    return nat_abun_list
