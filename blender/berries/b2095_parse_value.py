# parse_value
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file research/oee/pilots/run.py, line 34
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def parse_value(v: str):
    if v in ("true", "on"):
        return True
    if v in ("false", "off"):
        return False
    if "," in v or v.startswith("["):
        return [int(x) for x in v.strip("[]").split(",") if x]
    try:
        return int(v)
    except ValueError:
        try:
            return float(v)
        except ValueError:
            return v
