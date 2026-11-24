# person
#
# Copied verbatim from https://github.com/alexbarakov/amsterdam-by-building
#   file pipeline/s12_archive.py, line 105
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Historic cartography
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def person(name):
    """'Schaap, C.P.' and 'C.P. Schaap' both read as 'C.P. Schaap'."""
    if not name:
        return None
    if "," in name and "(" not in name.split(",")[0]:
        last, first = name.split(",", 1)
        first = first.split("(")[0].strip()
        return f"{first} {last.strip()}".strip()
    return name.split(" (")[0].strip()
