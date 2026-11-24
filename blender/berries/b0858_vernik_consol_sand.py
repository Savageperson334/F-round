# vernik_consol_sand
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/rockphysics/rockphysicsmodels.py, line 350
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def vernik_consol_sand(K0, G0, phi, sigma, b=10):
    '''
    Vernik & Kachanov Consolidated Sand Model.
    This model describes the elastic behaviour (K=bulk and G=shear moduli)
    of consolidated dry sand subject to a hydrostatic confining pressure
    as a continuous solid containing pores and cracks.

    Parameters
    ----------
    K0, G0 : float or array_like
        Mineral bulk & shear modulus in GPa.
    phi : float or array_like
        Porosity.
    sigma : float
        Effective stress in MPa.
    b : float, optional
        Slope parameter in pore shape empirical equation, range: 8-12.
        Default: 10.

    Returns
    -------
    Kdry, Gdry : float or array_like
        Dry rock bulk & shear modulus in GPa.

    References
    ----------
    Vernik & Kachanov (2010), Modeling elastic properties of siliciclastic rocks, Geophysics v.75 n.6
    '''
    # empirical pore shape factor:
    p = 3.6 + b * phi
    q = p # true if phi>0.03
    psf = phi / (1 - phi)  # psf = pore shape factor multiplier

    # matrix properties: assuming arenites with K=35.6 GPa, G=33 GPa, Poisson's ratio nu_m = 0.146
    nu_m = 0.146
    Avm = (16 * (1 - nu_m**2) ) / ( 9 * (1 - 2 * nu_m))       # nu_m=0.146 --> Avm=2.46
    Bvm = (32 * (1 - nu_m) * (5 - nu_m)) / (45 * (2 - nu_m))  # nu_m=0.146 --> Bvm=1.59

    # crack density: inversely correlated to effective stress
    eta0 = 0.3 + 1.6 * phi  # crack density at zero stress
    d = 0.07  # compaction coefficient
    d = 0.02 + 0.003 * sigma
    cd = (eta0 * np.exp(-d * sigma)) / (1 - phi)

    # note: the presence at denominator of the factor (1 - phi) in psf and cd is needed
    # to account for the interaction effects, i.e. the presence of pores raises the average stress
    # in the matrix increasing compliance contributions of pores and cracks
    # this correction is referred to as Mori-Tanaka's scheme.
    # in this way, the original model which is a NIA (non-interaction model)
    # is extended and becomes effectively a model which does take into account interactions.
    Kdry = K0 * (1 + p * psf + Avm * cd)**-1
    Gdry = G0 * (1 + q * psf + Bvm * cd)**-1
    return Kdry, Gdry
