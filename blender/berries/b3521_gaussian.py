# gaussian
#
# Copied verbatim from https://github.com/ricardodeazambuja/IJCNN2017
#   notebook 2DofArm_simulation_3D_printing_of_liquid_structure.ipynb (its code cells joined in order; line 183 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Robots and tactile mechanisms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy

input_gain=70


def gaussian(lamb,n,nt):
    '''
    Generates a gaussian centered at 'n'
    '''
    return input_gain*numpy.exp(-((nt-n)**2)/(2*(lamb)**2))
