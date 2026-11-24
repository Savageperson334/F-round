# type_name
#
# Copied verbatim from https://github.com/N6RFM/HADESx-Decoder
#   file src/hadesx/core.py, line 85
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

TYPE_NAMES = {1: 'Power', 2: 'Temperature', 3: 'Status', 4: 'Power stats',
              5: 'Temperature stats', 6: 'Sun sensors', 8: 'Antenna deploy',
              9: 'Extended power (INA)', 10: 'Nebrija game payload',
              12: 'Ephemeris', 14: 'Time series', 15: 'CODEC2 voice'}

TYPE_NAMES_BY_SOURCE = {
    3: {7: 'Experiment payload', 8: 'Antenna deploy', 9: 'Extended power (INA)', 10: 'SSDV image packet',
        11: 'CODEC2 voice', 12: 'Ephemeris', 13: 'PN9 link test', 14: 'Time series', 15: 'BBS message'},
    5: {7: 'Lofith payload', 8: 'Antenna deploy', 9: 'Extended power (INA)', 11: 'CODEC2 voice', 12: 'Ephemeris',
        13: 'PN9 link test', 14: 'Time series', 15: 'ICM message'},
}


def type_name(src, ptype):
    """Human-readable packet type for a source address."""
    return TYPE_NAMES_BY_SOURCE.get(src, {}).get(ptype) or TYPE_NAMES.get(ptype, '?')
