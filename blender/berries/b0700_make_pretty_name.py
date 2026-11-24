# make_pretty_name
#
# Copied verbatim from https://github.com/ScopeFoundry/ScopeFoundry
#   file tools/pages/new_hardware.py, line 99
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def make_pretty_name(model: str) -> str:
    s = model.split("_")
    if len(s) >= 2:
        name = "_".join(s[-2:])
    else:
        name = model
    return name.lower()
