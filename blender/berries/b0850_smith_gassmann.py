# smith_gassmann
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/rockphysics/fluidsub.py, line 56
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def smith_gassmann(kdry, k0, kf, phi):
    """
    Applies the direct Gassmann's equation to calculate the saturated rock
    bulk modulus from porosity and the dry-rock, mineral and fluid bulk moduli.

    Args:
        kdry (float): dry-rock bulk modulus.
        k0 (float): mineral bulk modulus.
        kf (float): fluid bulk modulus.
        phi (float): Porosity.

    Returns:
        ksat (float): saturated rock bulk modulus.
    """

    a = (1 - kdry/k0)**2.0
    b = phi/kf + (1-phi)/k0 - (kdry/k0**2.0)
    ksat = kdry + (a/b)

    return ksat
