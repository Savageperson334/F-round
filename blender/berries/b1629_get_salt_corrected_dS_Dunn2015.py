# get_salt_corrected_dS_Dunn2015
#
# Copied verbatim from https://github.com/douglaslab/pyOrigamiBreak
#   file autobreak/utilities.py, line 104
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Origami, folds and paper
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np

Mg_CONC      =  12.5E-3

TRIS_CONC    =  40.0E-3

EQN12_FACTOR = 0.368*np.log(0.5*TRIS_CONC + 3.3*np.sqrt(Mg_CONC))


def get_salt_corrected_dS_Dunn2015(seq_length):
    # Dunn et al. Equation 12
    # dSsalt = 0.368*(seq_length-1)*np.log(0.5*TRIS_CONC + 3.3*np.sqrt(Mg_CONC))
    dSsalt  = EQN12_FACTOR*(seq_length-1)
    return dSsalt
