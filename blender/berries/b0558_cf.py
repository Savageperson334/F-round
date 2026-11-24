# cf
#
# Copied verbatim from https://github.com/N6RFM/HADESx-Decoder
#   file src/hadesx/genesis.py, line 67
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def cf(v):
    """printf("%f") as the Windows tool (MinGW) prints it: NaN is "nan" whatever its sign (glibc would print "-nan")."""
    if v != v:
        return 'nan'
    return '%f' % v
