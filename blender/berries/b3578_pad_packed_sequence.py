# pad_packed_sequence
#
# Copied verbatim from https://github.com/seisbench/seisbench
#   file seisbench/util/arraytools.py, line 21
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def pad_packed_sequence(seq: list[np.ndarray]) -> np.ndarray:
    """
    Packs a list of arrays into one array by adding a new first dimension and padding where necessary.

    :param seq: List of numpy arrays
    :return: Combined arrays
    """
    max_size = np.array([max([x.shape[i] for x in seq]) for i in range(seq[0].ndim)])

    new_seq = []
    for i, elem in enumerate(seq):
        d = max_size - np.array(elem.shape)
        if (d != 0).any():
            pad = [(0, d_dim) for d_dim in d]
            new_seq.append(np.pad(elem, pad, "constant", constant_values=0))
        else:
            new_seq.append(elem)

    return np.stack(new_seq, axis=0)
