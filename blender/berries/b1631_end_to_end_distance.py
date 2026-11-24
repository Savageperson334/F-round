# end_to_end_distance
#
# Copied verbatim from https://github.com/douglaslab/pyOrigamiBreak
#   file autobreak/utilities.py, line 121
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Origami, folds and paper
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def end_to_end_distance(num_bases):
    '''
    Estimate end-to-end distance for DNA of length num_bases

    Model is from Rivetti et al. 1998, Eqn. 5
    https://www.sciencedirect.com/science/article/pii/S0022283698918307

    Constants are from Dunn et al. 2015, Eqn 12 
    https://www.nature.com/articles/nature14860 
    - Contour length L = 0.6 [nm]
    - Kuhn length λ_ss = 1.8 [nm]
    - Persistence length = λ_ss/2 = 0.9 [nm]
    '''
    L_base    = 0.6  # [nm]
    L_contour = num_bases*L_base
    L_p       = 0.9
    return 2*L_p*L_contour*(1-1.0*L_p/L_contour*(1-np.exp(-1.0*L_contour/L_p)))
