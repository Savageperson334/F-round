# normal
#
# Copied verbatim from https://github.com/alexbarakov/amsterdam-by-building
#   file pipeline/s14_search.py, line 21
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Historic cartography
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re
import unicodedata


def normal(s):
    """As normal() in app.js: lower case, no accents, runs of anything else become one space."""
    s = unicodedata.normalize("NFD", str(s).lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", s).strip()
