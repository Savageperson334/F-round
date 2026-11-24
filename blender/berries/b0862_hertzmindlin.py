# hertzmindlin
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/rockphysics/rpm.py, line 32
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
