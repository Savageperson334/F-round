# voltage_to_db
#
# Copied verbatim from https://github.com/Sebbe00/Hydrophone
#   file Färdig kod19majv3.py, line 63
#   licence (as GitHub reports it): CC0-1.0   see ../licenses/
#   catalogue shelf: Ocean hydrophones and acoustic ecology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def voltage_to_db(voltage):
    if voltage == 0:
        return 14  # return 14 dB at 0 volts
    else:
        # calculate dB for other voltages
        reference_voltage = 0.08  # voltage at 14 dB
        max_voltage = 1.024  # voltage at 120 dB
        min_db = 14
        max_db = 120
        slope = (max_db - min_db) / (max_voltage - reference_voltage)
        db = min_db + slope * (voltage - reference_voltage)
        return db
