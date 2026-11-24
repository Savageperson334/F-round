# distance_to_loop_dG
#
# Copied verbatim from https://github.com/douglaslab/pyOrigamiBreak
#   file autobreak/utilities.py, line 141
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Origami, folds and paper
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np

cal_per_J    = 1/4.184

R_SI_units   = 8.31447

kcal_per_cal = 0.001

R            = R_SI_units*cal_per_J*kcal_per_cal


def distance_to_loop_dG(distance_square, temperature_kelvin=323.15):
    '''Calculate loop entropy for distance_square, which has units of nm^2'''
    # Equation from https://www.nature.com/articles/nature14860 (doi:10.1038/nature14860)
    # Divide by 1000 to convert cal/(mol.K) to kcal/(mol.K)
    effective_concentration = 1.0/6.02E23*(3.0/(2*np.pi*distance_square*1E-18))**(3/2.0)/1000
    dSloop = R*np.log(effective_concentration)
    dGloop = -temperature_kelvin*dSloop

    return (dGloop, dSloop)
