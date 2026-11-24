# spectral_class
#
# Copied verbatim from https://github.com/tjyank/orrery-tui
#   file orrery/stellar/catalog.py, line 91
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def spectral_class(spectral: str) -> str:
    s = spectral[2:] if spectral.startswith("sd") else spectral
    return s[:1].upper() if s else "G"
