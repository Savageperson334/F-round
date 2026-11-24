# mps_to_kmph
#
# Copied verbatim from https://github.com/BoboTiG/thermalprinter
#   file src/thermalprinter/recipes/weather/__init__.py, line 452
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Thermal printers and obsolete output
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def mps_to_kmph(mps: float) -> int:
    """Convert the wind unity from m/sec to km/h.

    :param float mps: The input value in m/sec.
    :rtype: int
    :return: The converted value to km/h.
    """
    return int(mps * 3.6)
