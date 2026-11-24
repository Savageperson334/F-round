# reset_cause_name
#
# Copied verbatim from https://github.com/N6RFM/HADESx-Decoder
#   file src/hadesx/genesis.py, line 119
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def reset_cause_name(v):
    names = {0: 'Unknown', 1: 'Low Power Reset', 2: 'Window Watchdog reset', 3: 'Independent watchdog reset',
             4: 'Software reset', 5: 'Power-on reset (POR) / Power-down reset (PDR)', 6: 'External reset pin reset',
             7: 'Brownout reset (BOR)'}
    return names.get(v, 'TBD')
