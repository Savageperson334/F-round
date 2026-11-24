# o_code
#
# Copied verbatim from https://github.com/daniestevez/gr-satellites
#   file python/build_utils_codes.py, line 26
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#   the same function also appears in: kappiman/beesat-sdr
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def o_code(code3):
    if len(code3) >= 2:
        return code3[1]
    else:
        return code3[0]
