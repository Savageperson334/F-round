# signed_to_byte
#
# Copied verbatim from https://github.com/andrey-tut/LOOI-Robot
#   file looi_interactive_probe.py, line 32
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def signed_to_byte(value: int) -> int:
    value = max(-127, min(127, value))
    return value & 0xFF
