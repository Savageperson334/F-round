# archie_sw
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/petrophysics/petrophysics.py, line 203
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def archie_sw(phi, rw, rt, a=1, m=2, n=2):
    """
    Computes Archie water (fluid) saturation
    Args:
        a   (float): Cementation exponet, generally 1, 
              can range from ~0.5 to ~4 (empirical)
        m   (float): Cementation factor, commonly 2,
              decreases with more clay content (empirical)
        n   (float): Saturation exponet, commonly 2,
              generally ranges from 1.5 to 2.5 (empirical)
        rw  (float): Formation water (fluid) resistivity in ohmm
        rt  (float): Formation resistivity in ohmm
        phi (float): porosity, ranging from 0-1       

    Returns:
        ndarray: Water saturation estimation (Sw)
    """

    return ((a*rw)/(rt*phi**m))**(1/n)
