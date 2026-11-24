# convert_reservoir_to_raw_n
#
# Copied verbatim from https://github.com/DirtBurner/GeoChem_Class
#   file neuhaus_fcns.py, line 270
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math
import numpy as np

modern_ratio = 1.176810*10**(-12)


def convert_reservoir_to_raw_n(R):
    '''
    Converts from reservoir ages (something we all understand) to the raw numbers of 14C nuclides per 100 g of sediment
    required to run the Neuhaus et al model.

        Input variables:
            R (float or list of floats): postive integers representing the inherent of the modern ocean at the time of
                formation of a CaCO3 test or organic molecule from primary production. Lists can be accepted. 
        Ouput variables:
            n (float or list of floats): numbers on the magnitude of 10^(-18) which represent the number of 14C nuclides
                in 100 g of sediment. These numbers are necessary to run the Neuhaus model
    '''
    #Check for list:
    if type(R) is not list:
        print('Not a list - Variable R is a ', type(R), 'converting to a list.')
        if isinstance(R, int) and isinstance(R, float):
            print('Variable R is a ', type(R))
            R = [R]     #Makes it a list of one
        elif isinstance(R, np.ndarray):
            print('Variable is an ', type(R), '. Changing to list.')
            R = R.tolist()
        else:
            print("Must enter a float, integer, or a list of floats or integers. You entered a: ", type(R))
            return

    new_a = []
    A = 9*10**(-6)          #Accumulation rate of 12C, g/yr/100g sediment (from base conditions in paper)

    for ind, reservoir_age in enumerate(R):
        print(ind, reservoir_age)
        #Convert to fraction modern:
        F = math.exp(-reservoir_age/8033)
        #F is equal to the ratio of fluxes a/A, so we can calculate an a value for each F:
        new_a.append(F*modern_ratio*A)

    return new_a
