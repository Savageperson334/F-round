# layout_file
#
# Copied verbatim from https://github.com/jbschooley/Virtual-FM-1
#   file engines/choralroot/upstream/tools/gen_layout.py, line 90
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def layout_file(name):
    """fm1layout.js layoutFileName"""
    return re.sub(r"^-|-$", "", re.sub(r"[^a-z0-9]+", "-", name.lower())) + ".json"
