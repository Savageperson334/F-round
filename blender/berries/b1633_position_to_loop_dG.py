# position_to_loop_dG
#
# Copied verbatim from https://github.com/douglaslab/pyOrigamiBreak
#   file autobreak/utilities.py, line 153
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


def get_min_scaffold_distance(scaffold_length, start_index, end_index, is_scaffold_circular=True):
    '''Get min distance between two positions on a circular oligo'''
    forward_distance  = (end_index - start_index) % scaffold_length 
    reverse_distance = scaffold_length - forward_distance
    if is_scaffold_circular:
        return min(forward_distance, reverse_distance)
    else:
        return abs(end_index - start_index)


def position_to_loop_dG(scaffold_length, start_index, end_index, scaffold_circular=True, 
                        temperature_kelvin=323.15):
    # Get number of minimum number of bases between to location
    base_distance  = get_min_scaffold_distance(scaffold_length, start_index, end_index, scaffold_circular)

    # Determine end to end distance^2
    distance_square = end_to_end_distance(base_distance)

    # Get the free energies
    energies = distance_to_loop_dG(distance_square, temperature_kelvin)

    return energies
