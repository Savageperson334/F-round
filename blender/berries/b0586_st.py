# st
#
# Copied verbatim from https://github.com/N6RFM/HADESx-Decoder
#   file tools/build_grc.py, line 218
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def st(x, y):
    return ('  states:\n    bus_sink: false\n    bus_source: false\n    bus_structure: null\n'
            '    coordinate: [%d, %d]\n    rotation: 0\n    state: enabled\n' % (x, y))
