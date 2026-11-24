# softsand
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/rockphysics/rpm.py, line 55
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def hertzmindlin(K0, G0, phi, phic=0.4, Cn=8.6, P=10, f=1):
    '''
    Hertz-Mindlin model
    written by Alessandro Amato del Monte (2015)
    from Mavko et al., Rock Physics Handbook, p.246

    Args:
        K0, G0: mineral bulk & shear modulus in GPa
        phi: porosity
        phic: critical porosity (default 0.4)
        Cn: coordination nnumber (default 8.6)
        P: confining pressure in MPa (default 10)
        f: shear modulus correction factor, f=1 for dry pack with perfect adhesion between particles and f=0 for dry frictionless pack.

    Returns:
        Tuple: K_DRY, G_DRY: dry rock bulk & shear modulus in GPa
    '''
    P /= 1e3 # converts pressure in same units as solid moduli (GPa)
    PR0=(3*K0-2*G0)/(6*K0+2*G0) # poisson's ratio of mineral mixture
    K_HM = (P*(Cn**2*(1-phic)**2*G0**2) / (18*np.pi**2*(1-PR0)**2))**(1/3)
    G_HM = ((2+3*f-PR0*(1+3*f))/(5*(2-PR0))) * ((P*(3*Cn**2*(1-phic)**2*G0**2)/(2*np.pi**2*(1-PR0)**2)))**(1/3)
    return K_HM, G_HM


def softsand(K0, G0, phi, phic=0.4, Cn=8.6, P=10, f=1):
    '''
    Soft-sand (uncemented) model
    written by Alessandro Amato del Monte (2015)
    from Mavko et al., Rock Physics Handbook, p.258

    Args:
        K0, G0: mineral bulk & shear modulus in GPa
        phi: porosity
        phic: critical porosity (default 0.4)
        Cn: coordination nnumber (default 8.6)
        P: confining pressure in MPa (default 10)
        f: shear modulus correction factor, f=1 for dry pack with perfect adhesion between particles and f=0 for dry frictionless pack

    Returns:
        Tuple: K_DRY, G_DRY: dry rock bulk & shear modulus in GPa
    '''
    K_HM, G_HM = hertzmindlin(K0, G0, phi, phic, Cn, P, f)
    K_DRY =-4/3*G_HM + (((phi/phic)/(K_HM+4/3*G_HM)) + ((1-phi/phic)/(K0+4/3*G_HM)))**-1
    tmp = G_HM/6*((9*K_HM+8*G_HM) / (K_HM+2*G_HM))
    G_DRY = -tmp + ((phi/phic)/(G_HM+tmp) + ((1-phi/phic)/(G0+tmp)))**-1
    return K_DRY, G_DRY
