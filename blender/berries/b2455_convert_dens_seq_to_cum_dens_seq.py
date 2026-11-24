# convert_dens_seq_to_cum_dens_seq
#
# Copied verbatim from https://github.com/jlanversin/ONIX
#   file onix/utils/data_processor.py, line 1004
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def convert_dens_seq_to_cum_dens_seq(dens_seq):

    cum_dens_seq = []
    cum_dens_seq.append(dens_seq[0])
    for i in range(1, len(dens_seq)):
        cum_dens_seq.append(dens_seq[i] + cum_dens_seq[i-1])

    return cum_dens_seq
