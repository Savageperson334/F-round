# caption_num_animals
#
# Copied verbatim from https://github.com/david-rx/BioLingual
#   file animalspeak/process_watkins.py, line 102
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def caption_num_animals(caption, num_animals):
    try:
        num = int(num_animals)
        if num == 1:
            caption += "a "
        else:
            caption += f"{num} "
    except ValueError:
        # num_animals could not be converted to an integer, so just return the original caption
        return caption + f"{num_animals} "
    return caption
