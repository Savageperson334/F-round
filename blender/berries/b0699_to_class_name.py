# to_class_name
#
# Copied verbatim from https://github.com/ScopeFoundry/ScopeFoundry
#   file tools/features/utils.py, line 22
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from re import sub


def to_class_name(s: str) -> str:
    s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
    return "".join([s[0].upper(), s[1:]])
