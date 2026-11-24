# quote
#
# Copied verbatim from https://github.com/chrisfulcher/orrery
#   file src/orrery/dotenv.py, line 57
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def quote(value: str | None) -> str:
    """A value as ``.env`` readers expect: bare when plain, double-quoted otherwise."""
    if value is None or value == "":
        return ""
    if re.fullmatch(r"[A-Za-z0-9_./:@+,%~-]+", value):
        return value
    escaped = value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
    return f'"{escaped}"'
