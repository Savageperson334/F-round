# vernik_soft_sand_2
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/rockphysics/rockphysicsmodels.py, line 460
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def vernik_soft_sand_2(K0, G0, phi, p=20, q=20):
    '''
    Vernik & Kachanov Soft Sand Model 2.
    This model describes the elastic behaviour (K=bulk and G=shear moduli)
    of dry sand modeled as a granular material.
    Applicable in the entire porosity range.

    Parameters
    ----------
    K0, G0 : float or array_like
        Mineral bulk & shear modulus in GPa.
    phi : float or array_like
        Porosity.
    p, q : float, optional
        Pore shape factor for K and G, range: 10-45.
        Default: 20.

    Returns
    -------
    Kdry, Gdry : float or array_like
        Dry rock bulk & shear modulus in GPa.

    References
    ----------
    Vernik & Kachanov (2010), Modeling elastic properties of siliciclastic rocks, Geophysics v.75 n.6
    '''
    M0 = K0 + 4/3 * G0
    Mdry = M0 * (1 + p * (phi / (1 - phi)))**-1
    Gdry = G0 * (1 + q * (phi / (1 - phi)))**-1
    Kdry = Mdry - 4/3 * Gdry
    return Kdry, Gdry
