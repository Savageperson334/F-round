# transponder_mode
#
# Copied verbatim from https://github.com/N6RFM/HADESx-Decoder
#   file src/hadesx/genesis.py, line 136
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def transponder_mode(v, hades_l=False):
    return {0: '         Disabled', 1: '         Enabled in USB->FM mode' if hades_l else '         Enabled in FM mode',
            2: '         Enabled in FSK regenerative mode'}.get(v, '         Unknown')
