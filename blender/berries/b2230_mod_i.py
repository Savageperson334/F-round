# mod_i
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/utility.py, line 1269
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def mod_i(i, cycle):
    """
    Calculates modulus of a function and returns number of full cycles and the
    rest.

    Parameters
    ----------
    i : int or float
        Number to be cycled over
    cycle : int o float
        Cycle length

    Returns
    -------
    fullc : int or float depending on input
    rest : int or float depending on input
    """
    fullc = i // cycle
    rest = i % cycle
    return fullc, rest
