# map_to_common_name
#
# Copied verbatim from https://github.com/david-rx/BioLingual
#   file animalspeak/process_watkins.py, line 89
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def map_to_common_name(species_name):
    # Special case for names containing parenthesis
    if "LongBeaked" in species_name:
        return "Long Beaked (Pacific) Common Dolphin"

    # Split at capital letters, except at the start of a string or preceded by an underscore
    parts = re.findall('[a-zA-Z][^A-Z]*', species_name)

    # Join the parts with a space and replace underscore with hyphen
    common_name = " ".join(parts).replace("_", "-")

    return common_name
