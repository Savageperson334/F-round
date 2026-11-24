# sampled_index
#
# Copied verbatim from https://github.com/jlanversin/ONIX
#   file onix/nax/functions.py, line 1124
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import itertools
import math as m


def sampled_index(batch_break_indexes):

    point_per_batch = 5

    previous_break_index = 0
    sampled_index_list = []
    for i in range(len(batch_break_indexes)):
        break_index = batch_break_indexes[i]
        int_length = break_index - previous_break_index
        step = m.floor(int_length/point_per_batch)
        batch_sampled_index = [j*step + previous_break_index for j in range(point_per_batch)] +[break_index-1]
        previous_break_index = break_index
        sampled_index_list.append(batch_sampled_index)

    sampled_index = list(itertools.chain.from_iterable(sampled_index_list))


    return sampled_index
