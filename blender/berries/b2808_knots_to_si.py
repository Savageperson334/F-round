# knots_to_si
#
# Copied verbatim from https://github.com/mtomasini/PytheasSimulator
#   file src/pytheas_simulator/utilities.py, line 53
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def knots_to_si(knots: float) -> float:
    """Converts knots to SI units (m/s)

    Args:
        knots (float): Speed in knots

    Returns:
        float: Speed in metres/second
    """

    return knots / 1.94384
