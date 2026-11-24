# log_add
#
# Copied verbatim from https://github.com/isi-vista/VistaOCR
#   file src/models/cnnlstm.py, line 22
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def log_add(logx, logy):
    if (logy > logx):
        temp = logx
        logx = logy
        logy = temp

    negdiff = logy - logx

    if negdiff < -20:
        return logx

    return logx + np.log(1.0 + np.exp(negdiff))
