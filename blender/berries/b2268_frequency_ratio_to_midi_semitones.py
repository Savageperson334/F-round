# frequency_ratio_to_midi_semitones
#
# Copied verbatim from https://github.com/ideoforms/isobar
#   file isobar/util.py, line 204
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sound sonification
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def frequency_ratio_to_midi_semitones(frequency_ratio) -> float:
    """
    Map a given frequency ratio to the corresponding interval, in semitones.

    Args:
        frequency_ratio: The frequency ratio.

    Returns:
        float: The ratio, in semitones
    """
    return math.log2(frequency_ratio) * 12
