# lambda_transition
#
# Copied verbatim from https://github.com/worm-portal/pychnosz
#   file pychnosz/models/cgl.py, line 291
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Metrology, microscopes and geology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def lambda_transition(T: np.ndarray, T_lambda: float, lambda_val: float, 
                     sigma: float = 50.0):
    """
    Calculate lambda transition contributions to thermodynamic properties.

    Parameters
    ----------
    T : array
        Temperature in Kelvin
    T_lambda : float
        Lambda transition temperature in Kelvin
    lambda_val : float
        Lambda transition parameter
    sigma : float
        Width parameter for transition (default: 50 K)

    Returns
    -------
    dict
        Dictionary with lambda contributions to Cp, H, S, G
    """

    # Gaussian approximation for lambda transition
    gaussian = np.exp(-(T - T_lambda)**2 / (2 * sigma**2))

    # Heat capacity contribution
    Cp_lambda = lambda_val * gaussian

    # Enthalpy contribution (integrated Cp)
    H_lambda = np.where(T > T_lambda, 
                       lambda_val * sigma * np.sqrt(2*np.pi) * 0.5 * (1 + np.tanh((T-T_lambda)/sigma)),
                       0)

    # Entropy contribution (integrated Cp/T)
    S_lambda = np.where(T > T_lambda, lambda_val / T_lambda, 0)

    # Gibbs energy contribution
    G_lambda = H_lambda - T * S_lambda

    return {
        'Cp': Cp_lambda,
        'H': H_lambda, 
        'S': S_lambda,
        'G': G_lambda
    }
