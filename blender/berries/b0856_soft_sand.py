# soft_sand
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/rockphysics/rockphysicsmodels.py, line 92
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def hertz_mindlin(K0, G0, sigma, phi_c=0.4, Cn=8.6, f=1):
    '''
    Hertz-Mindlin model.
    This model describes the elastic behaviour (K=bulk and G=shear moduli)
    of a dry pack of spheres subject to a hydrostatic confining pressure. 

    Parameters
    ----------   
    K0, G0 : float or array_like
        Mineral bulk & shear modulus in GPa.
    phi : float or array_like
        Porosity.
    sigma : float
        Effective stress in MPa.
    phi_c : float, optional
        Critical porosity. Default: 0.4
    Cn : float, optional
        Coordination number Default: 8.6.
    f : float, optional
        Shear modulus correction factor,
        f=1 for dry pack with perfect adhesion
        between particles and f=0 for dry frictionless pack.

    Returns
    -------
    Kdry, Gdry : float or array_like
        Dry rock bulk & shear modulus in GPa.

    References
    ----------
    Mavko et al. (2009), The Rock Physics Handbook, Cambridge University Press (p.246)
    '''
    sigma0 = sigma / 1e3  # converts pressure in same units as solid moduli (GPa)
    pr0 =(3*K0-2*G0) / (6*K0+2*G0)  # poisson's ratio of mineral mixture
    Khm = (sigma0*(Cn**2*(1 - phi_c)**2*G0**2) / (18
        * np.pi**2 * (1 - pr0)**2))**(1/3)
    Ghm = ((2+3*f-pr0*(1+3*f)) / (5*(2-pr0))) * ((
        sigma0 * (3 * Cn**2 * (1 - phi_c)**2 * G0**2) / (
        2 * np.pi**2 * (1 - pr0)**2)))**(1/3)
    return Khm, Ghm


def soft_sand(K0, G0, phi, sigma, phi_c=0.4, Cn=8.6, f=1):
    '''
    Soft sand, or friable sand or uncemented sand model.
    This model describes the elastic behaviour (K=bulk and G=shear moduli)
    of poorly sorted dry sand by interpolating with the lower Hashin-Shtrikman bound
    the two end members at zero porosity and critical porosity.
    The zero porosity end member has K and G equal to mineral.
    The end member at critical porosity has K and G given by Hertz-Mindlin model.

    Parameters
    ----------   
    K0, G0 : float or array_like
        Mineral bulk & shear modulus in GPa.
    phi : float or array_like
        Porosity.
    sigma : float
        Effective stress in MPa.
    phi_c : float, optional
        Critical porosity. Default: 0.4
    Cn : float, optional
        Coordination number Default: 8.6.
    f : float, optional
        Shear modulus correction factor,
        f=1 for dry pack with perfect adhesion
        between particles and f=0 for dry frictionless pack.

    Returns
    -------
    Kdry, Gdry : float or array_like
        Dry rock bulk & shear modulus in GPa.

    References
    ----------
    Mavko et al. (2009), The Rock Physics Handbook, Cambridge University Press (p.258)
    '''
    Khm, Ghm = hertz_mindlin(K0, G0, sigma, phi_c, Cn, f)
    Kdry = -4/3 * Ghm + (((phi / phi_c) / (Khm + 4/3 * Ghm))
        + ((1 - phi / phi_c) / (K0 + 4/3 * Ghm)))**-1
    gxx = Ghm / 6 * ((9 * Khm + 8 * Ghm)  /  (Khm + 2 * Ghm))
    Gdry = -gxx + ((phi / phi_c) / (Ghm + gxx)
        + ((1 - phi / phi_c) / (G0 + gxx)))**-1
    return Kdry, Gdry
