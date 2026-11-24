# contrast
#
# Copied verbatim from https://github.com/dnet/pySSTV
#   file pysstv/examples/gimp-plugin.py, line 149
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Strange radio, signals and transmissions
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def contrast(value):
    if 80 < value < 160:
        return value + (80 if value < 120 else -80)
    else:
        return 255 - value
