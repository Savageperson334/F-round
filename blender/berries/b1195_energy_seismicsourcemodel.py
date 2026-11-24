# energy_seismicsourcemodel
#
# Copied verbatim from https://github.com/bqpseismology/seismology
#   file src/seismology/source.py, line 558
#   licence (as GitHub reports it): MPL-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def energy_seismicsourcemodel(G, XYZ) :    
    """
    Evaluate statistical properties of the given seismic wave radiation 
    pattern.
    ______________________________________________________________________
    :type G : 3D array, list | np.array
    :param G : The vector of cartessian coordinates of the radiation 
        pattern.

    :type XYZ : 3D array, list | np.array
    :param XYZ : The cartessian coordinates of the origin points of the
        radiation pattern.

    :rtype : list
    :return : The statistical properties of amplitudes [rms, euclidian norm, average].

    .. todo::

        Compute more properties, add request handling.
    ______________________________________________________________________
    """

    #amplitudes_correction = np.sum(G * XYZ, axis=0)
    #amplitudes_correction /= np.max(np.abs(amplitudes_correction))
    amplitudes = np.sqrt( G[0]**2 + G[1]**2 + G[2]**2 ) #* amplitudes_correction            

    # Classic rms
    rms = np.sum(amplitudes**2)/np.prod(amplitudes.shape)  
    # Euclidian norm
    norm = np.sqrt(np.sum(amplitudes**2))  
    # Amplitude average
    average = np.average(np.abs(amplitudes))  

    return [rms, norm, average]
