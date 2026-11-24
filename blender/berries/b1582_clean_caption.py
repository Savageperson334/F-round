# clean_caption
#
# Copied verbatim from https://github.com/david-rx/BioLingual
#   file CLAP/src/laion_clap/training/train.py, line 598
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def clean_caption(caption):
    if caption.startswith("The sound of a "):
        caption = caption[len("The sound of a "):]
    elif caption.startswith("The sound of an "):
        caption = caption[len("The sound of an "):]
    return caption.strip()
