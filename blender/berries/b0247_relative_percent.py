# relative_percent
#
# Copied verbatim from https://github.com/Fountain-Coach/blackmagic-intensity-extreme-revival
#   file tools/sierra/hdmi-output-clock-witness.py, line 31
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def relative_percent(actual, nominal):
    if nominal <= 0:
        raise ValueError("nominal must be positive")
    return 100.0 * (actual / nominal - 1.0)
