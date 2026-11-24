# midi_semitones_to_frequency_ratio
#
# Copied verbatim from https://github.com/ideoforms/isobar
#   file isobar/util.py, line 191
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sound sonification
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def midi_semitones_to_frequency_ratio(semitones: list[float]) -> float:
    """
    Map a MIDI semitone interval to a frequency ratio
    (e.g., input of 12 semitones -> output of 2.0)

    Args:
        semitones: The pitch difference, in semitones

    Returns:
        float: The frequency ratio corresponding to the semitone interval.
    """
    return pow(2, semitones / 12.0)
