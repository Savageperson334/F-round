# rewrite_data_path
#
# Copied verbatim from https://github.com/microsoft/haste
#   file native/gdal-runtime/assemble_wheels.py, line 123
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def rewrite_data_path(path: str, staging_data_prefix: str) -> str:
    """Map a wheel's .data tree into the staging wheel's .data tree."""
    match = re.match(r"[^/]+\.data/(.+)$", path)
    if match:
        return f"{staging_data_prefix}/{match.group(1)}"
    return path
