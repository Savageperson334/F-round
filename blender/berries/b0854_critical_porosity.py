# critical_porosity
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/rockphysics/rockphysicsmodels.py, line 15
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def critical_porosity(K0, G0, phi, phi_c=0.4):
    '''
    Critical porosity model.
    This model describes the elastic behaviour (K=bulk and G=shear moduli)
    of dry sand for porosities below the critical porosity (phi_c).
    Above phi_c, the fluid phase is load-bearing, below phi_c the
    solid phase (mineral grains) is load-bearing.
    The equations here describe the variation of K and G
    for porosities below phi_c as straight lines.
    Critical porosity is usually 0.4 for sandstone,
    0.7 for chalk, 0.02-0.03 for granites.

    Parameters
    ----------   
    K0, G0 : float or array_like
        Mineral bulk & shear modulus in GPa.
    phi : float or array_like
        Porosity.
    phi_c : float, optional
        Critical porosity. Default: 0.4

    Returns
    -------
    Kdry, Gdry : float or array_like
        Dry rock bulk & shear modulus in GPa.

    References
    ----------
    Mavko et al. (2009), The Rock Physics Handbook, Cambridge University Press (p.370)
    '''
    Kdry = K0 * (1 - phi / phi_c)
    Gdry = G0 * (1 - phi / phi_c)
    return Kdry, Gdry
