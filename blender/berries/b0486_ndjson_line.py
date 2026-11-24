# ndjson_line
#
# Copied verbatim from https://github.com/MacNite/HiveHub
#   file server/data_export.py, line 136
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Beehives and unusual agriculture
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import json


def ndjson_line(record: dict) -> str:
    """Serialize one record as a newline-terminated NDJSON line."""
    return json.dumps(record, separators=(",", ":"), default=str) + "\n"
