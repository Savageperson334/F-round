# hamming_weight
#
# Copied verbatim from https://github.com/daniestevez/gr-satellites
#   file python/components/deframers/openlst_deframer.py, line 37
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def hamming_weight(byte: int) -> int:
    """Return the number of one bits in a byte"""
    return sum(int(b) for b in f"{byte:b}")
