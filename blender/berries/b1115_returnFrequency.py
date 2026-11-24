# returnFrequency
#
# Copied verbatim from https://github.com/awalmer/Sonification-Exercises
#   file NYC Evictions/Jupyter/MidiFile.py, line 1799
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sound sonification
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def returnFrequency(freqBytes):
    '''
    The reverse of frequencyTransform. Given a byte stream, return a frequency.
    '''
    resolution = 16384.0
    baseFrequency = 440 * pow(2.0, (float(freqBytes[0] - 69.0) / 12.0))
    frac = (float((int(freqBytes[1]) << 7) + int(freqBytes[2])) * 100.0) / resolution
    frequency = baseFrequency * pow(2.0, frac / 1200.0)
    return frequency
