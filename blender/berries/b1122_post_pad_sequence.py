# post_pad_sequence
#
# Copied verbatim from https://github.com/axcelerateai/urdu-handwriting-recognition-using-deep-learning
#   file utils/helpers.py, line 37
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import copy


def post_pad_sequence(seq, max_len, value=0):
    seq_copy = list(copy.deepcopy(seq))
    add_zeros = max_len - len(seq_copy)
    new_seq = [value for i in range(add_zeros)]
    seq_copy.extend(new_seq)

    return seq_copy
