# robust_split
#
# Copied verbatim from https://github.com/Molara-Lab/Molara
#   file src/molara/structure/io/importer_crystal.py, line 24
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def robust_split(text: str) -> list[str]:
    """Split a text into its components (separated by any kinds of space characters) with regular expressions.

    :param text: text to be split up
    """
    return re.split(r"\s+", text)
