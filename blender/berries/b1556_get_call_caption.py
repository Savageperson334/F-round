# get_call_caption
#
# Copied verbatim from https://github.com/david-rx/BioLingual
#   file animalspeak/process_watkins.py, line 114
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

SIGNAL_TYPE_MAPPING = {
        'BL': 'broadband long signals',
        'BS': 'broadband short signals',
        'NL': 'narrowband long signals',
        'NS': 'narrowband short signals',
        'FM': 'frequency modulated signals',
        'CH': 'chirp signals',
        'PU': 'pulsed signals',
        'SE': 'series of sounds',
        'SO': 'song signals',
    }


def get_call_caption(caption, signal_type):
    if signal_type and signal_type in SIGNAL_TYPE_MAPPING:
            caption += f"{SIGNAL_TYPE_MAPPING[signal_type]} of "
    else:
        caption += "Sound of "
    return caption
