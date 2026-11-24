# monster_count
#
# Copied verbatim from https://github.com/alepersichetti/WyrmHex
#   file wyrmhex.py, line 5132
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Cave surveys and subterranean maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

ENCOUNTER_DIE = 20

STORY_ENCOUNTERS = 6


def monster_count(history):
    """How many of the 20 rows are monsters: all, or all but the story ones."""
    return ENCOUNTER_DIE - (STORY_ENCOUNTERS if history else 0)
