# restore_data_path
#
# Copied verbatim from https://github.com/microsoft/haste
#   file native/gdal-runtime/assemble_wheels.py, line 131
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def normalized_name(value: str) -> str:
    return re.sub(r"[-_.]+", "_", value).lower()


def restore_data_path(path: str, name: str, version: str) -> str:
    """Give a .data member the matching output wheel's name and version."""
    match = re.match(r"[^/]+\.data/(.+)$", path)
    if match:
        prefix = f"{normalized_name(name)}-{version}.data"
        return f"{prefix}/{match.group(1)}"
    return path
