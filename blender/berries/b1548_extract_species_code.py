# extract_species_code
#
# Copied verbatim from https://github.com/david-rx/BioLingual
#   file animalspeak/process_watkins.py, line 49
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def extract_species_code(genus_species):
    first_section = genus_species.split(" | ")[0]
    species_code = first_section.split(" ")[-1]
    scientific_name = " ".join(first_section.split(" ")[:-1]).strip()
    return scientific_name, species_code
