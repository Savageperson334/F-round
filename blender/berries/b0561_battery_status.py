# battery_status
#
# Copied verbatim from https://github.com/N6RFM/HADESx-Decoder
#   file src/hadesx/genesis.py, line 126
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def battery_status(v):
    return {0: 'Fully charged (3925 mV or higher) - All transmissions high power',
            1: 'High charge (Between 3800 mV and 3925 mV)',
            2: 'Charged (Between 3550 mV and 3800 mV) - Transmissions in low power',
            3: 'Low charge (Between 3300 mV and 3550 mV) - Limited transmissions and in low power',
            4: 'Very low charge (Between 3200 mV and 3300 mV) - Limited transmissions and in low power',
            5: 'Extremely low charge (Between 2500 mV and 3200 mV) - Limited transmissions and in  low power',
            6: 'Battery damaged (Below 2500 mV) - Battery disconnected'}.get(v, 'Unknown')
