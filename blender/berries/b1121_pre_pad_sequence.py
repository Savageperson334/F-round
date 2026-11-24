# pre_pad_sequence
#
# Copied verbatim from https://github.com/axcelerateai/urdu-handwriting-recognition-using-deep-learning
#   file utils/helpers.py, line 29
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def pre_pad_sequence(seq, max_len, value=0):
    add_zeros = max_len - len(seq)
    new_seq = [value for i in range(add_zeros)]
    new_seq.extend(seq)

    return new_seq
