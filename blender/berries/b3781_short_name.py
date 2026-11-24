# short_name
#
# Copied verbatim from https://github.com/tjyank/orrery-tui
#   file orrery/lookup.py, line 81
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def short_name(full_name: str) -> str:
    """'99942 Apophis (2004 MN4)' -> 'Apophis'; '1P/Halley' -> 'Halley'; 'Hale-Bopp (C/1995 O1)' -> 'Hale-Bopp'."""
    name = re.sub(r"\s*\(.*\)\s*$", "", full_name).strip()  # a trailing (designation)
    if not re.fullmatch(r"\d{4}\s+[A-Z]{1,2}\d*", name):  # leave a designation like "2004 MN4" whole
        name = re.sub(r"^\d+\s+(?=\D)", "", name)  # a leading catalogue number
    name = re.sub(r"^\d+[PDI]/", "", name)  # a periodic comet's number
    return name or full_name.strip()
