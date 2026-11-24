# normalize_class_name
#
# Copied verbatim from https://github.com/microsoft/haste
#   file docker/training/code/bda/config.py, line 137
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def normalize_class_name(name: str) -> str:
    """Fold a class name to a form that survives casing and separator drift.

    "No Damage", "no_damage", "NO-DAMAGE" and "no  damage" all normalize to
    the same string.

    Args:
        name (str): A class name from the config.

    Returns:
        str: The normalized name.
    """
    return re.sub(r"[\s_\-]+", " ", str(name).strip().casefold())
