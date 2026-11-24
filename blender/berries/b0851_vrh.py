# vrh
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/rockphysics/fluidsub.py, line 78
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def vrh(kclay, kqtz, vclay):
    """
    Voigt-Reuss-Hill average to find Kmatrix from clay and qtz components.
    Works for any two components, they don't have to be clay and quartz.

    From Smith et al, Geophysics 68(2), 2003.

    Args:
        kclay (float): K_clay.
        kqtz (float): K_quartz.
        vclay (float): V_clay.

    Returns:
        Kvrh, also known as Kmatrix.
    """

    vqtz = 1 - vclay

    kreuss = 1. / (vclay/kclay + vqtz/kqtz)
    kvoigt = vclay*kclay + vqtz*kqtz
    kvrh = 0.5 * (kreuss + kvoigt)

    return kvrh
