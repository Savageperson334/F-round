# normalize_class_name
#
# Copied verbatim from https://github.com/microsoft/haste
#   file hastelib/src/hastegeo/core/utils/label_classes.py, line 38
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def normalize_class_name(name: str) -> str:
    """Fold a class name so casing and separator style don't matter.

    "No Damage", "no_damage", "NO-DAMAGE" and "no  damage" all normalize to
    the same string. This matches the case-insensitive duplicate check the
    project form already applies (``validatePrimaryClasses`` in
    ``ui/src/util/validation.js``).

    Args:
        name (str): A class name.

    Returns:
        str: The normalized name.
    """
    return re.sub(r"[\s_\-]+", " ", str(name).strip().casefold())
