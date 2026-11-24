# append_end_token
#
# Copied verbatim from https://github.com/axcelerateai/urdu-handwriting-recognition-using-deep-learning
#   file utils/helpers.py, line 7
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def append_end_token(y, token_id, except_max=False):
    if except_max:
        max_len = max([len(yi) for yi in y])
        new_y = []
        for yi in y:
            if len(yi) != max_len:
                new_y.append(np.append(yi, token_id))
            else:
                new_y.append(yi)
        y = new_y
    else:
        y = [np.append(yi, token_id) for yi in y]

    return y
