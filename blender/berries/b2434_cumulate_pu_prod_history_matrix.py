# cumulate_pu_prod_history_matrix
#
# Copied verbatim from https://github.com/jlanversin/ONIX
#   file onix/nax/functions.py, line 755
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def cumulate_pu_prod_history_matrix(concatenate_pu_prod_history_matrix):

    cumulate_pu_prod_history_matrix = []

    for dens_seq in concatenate_pu_prod_history_matrix:
        cum_dens_seq = []
        cum_dens_seq.append(dens_seq[0])
        for dens in dens_seq[1:]:
            cum_dens = dens + cum_dens_seq[-1]
            cum_dens_seq.append(cum_dens)

        cumulate_pu_prod_history_matrix.append(cum_dens_seq)

    return cumulate_pu_prod_history_matrix
