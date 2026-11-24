# critpor
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/rockphysics/rpm.py, line 11
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def critpor(K0, G0, phi, phic=0.4):
    """
    Critical porosity, Nur et al. (1991, 1995) written by Alessandro Amato
    del Monte (2015) from Mavko et al., Rock Physics Handbook, p.353.

    Args:
        K0, G0: float or array_like
            Mineral bulk & shear modulus in GPa
        phi: float or array_like
            porosity
        phic: float or array_like
            critical porosity (default 0.4)

    Returns:
        Tuple: K_DRY, G_DRY: dry rock bulk & shear modulus in GPa
    """
    K_DRY  = K0 * (1-phi/phic)
    G_DRY  = G0 * (1-phi/phic)
    return K_DRY, G_DRY
