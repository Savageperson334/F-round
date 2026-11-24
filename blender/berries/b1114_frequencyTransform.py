# frequencyTransform
#
# Copied verbatim from https://github.com/awalmer/Sonification-Exercises
#   file NYC Evictions/Jupyter/MidiFile.py, line 1779
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sound sonification
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def frequencyTransform(freq):
    '''
    Returns a three-byte transform of a frequency.
    '''
    resolution = 16384
    freq = float(freq)
    dollars = 69 + 12 * math.log(freq / (float(440)), 2)
    firstByte = int(dollars)
    lowerFreq = 440 * pow(2.0, ((float(firstByte) - 69.0) / 12.0))
    centDif = 1200 * math.log((freq / lowerFreq), 2) if freq != lowerFreq else 0
    cents = round(centDif / 100 * resolution)  # round?
    secondByte = min([int(cents) >> 7, 0x7F])
    thirdByte = cents - (secondByte << 7)
    thirdByte = min([thirdByte, 0x7f])
    if thirdByte == 0x7f and secondByte == 0x7F and firstByte == 0x7F:
        thirdByte = 0x7e
    thirdByte = int(thirdByte)
    return [firstByte, secondByte, thirdByte]
