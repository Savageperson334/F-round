# ValueToBool
#
# Copied verbatim from https://github.com/projecthorus/horus-gui
#   file horusgui/config.py, line 48
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def ValueToBool(Value):
    """ Helper function to deal with QSettings inconsistency in handling boolean values """
    if isinstance(Value, bool):
        RetVal = Value
    else:
        RetVal = None
        if isinstance(Value, str):
            if Value.lower() == 'true':
                RetVal = True
            elif Value.lower() == 'false':
                RetVal = False
        else:
            RetVal = bool(Value)

    return RetVal
