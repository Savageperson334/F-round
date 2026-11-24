# si_to_knots
#
# Copied verbatim from https://github.com/mtomasini/PytheasSimulator
#   file src/pytheas_simulator/utilities.py, line 66
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def si_to_knots(si: float) -> float:
    """Converts SI units (m/s) to knots

    Args:
        si (float): Speed in m/s

    Returns:
        float: Speed in knots
    """

    return si * 1.94384
