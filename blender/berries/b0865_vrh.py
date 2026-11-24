# vrh
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/rockphysics/rpt.py, line 16
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def vrh(volumes,k,mu):
    '''
    Calculates Voigt-Reuss-Hill bounds.

    Args:
        volumes: array with volumetric fractions
        k: array with bulk modulus
        mu: array with shear modulus

    Returns:
        k_u, k_l: upper (Voigt) and lower (Reuss) average for k
        mu_u, mu_l: upper (Voigt) and lower (Reuss) average for mu
        k0, mu0: Hill average of k and mu
    '''
    f=np.array(volumes).T
    k=np.resize(np.array(k),np.shape(f))
    mu=np.resize(np.array(mu),np.shape(f))
    ax=0 if f.ndim==1 else 1
    k_u = np.sum(f*k,axis=ax)
    k_l = 1./np.sum(f/k,axis=ax)
    mu_u = np.sum(f*mu,axis=ax)
    mu_l = 1./np.sum(f/mu,axis=ax)
    k0 = (k_u+k_l)/2.
    mu0 = (mu_u+mu_l)/2.
    return k_u, k_l, mu_u, mu_l, k0, mu0
