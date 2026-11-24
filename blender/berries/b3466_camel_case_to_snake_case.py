# camel_case_to_snake_case
#
# Copied verbatim from https://github.com/pyrocko/qseek
#   file src/qseek/utils.py, line 756
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def camel_case_to_snake_case(name: str) -> str:
    """Converts a camel case string to snake case.

    Args:
        name (str): The camel case string to be converted.

    Returns:
        str: The snake case string.

    Example:
        >>> camel_case_to_snake_case("camelCaseString")
        'camel_case_string'
    """
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()
