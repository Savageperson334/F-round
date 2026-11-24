# mark_buildings
#
# Copied verbatim from https://github.com/alexbarakov/amsterdam-by-building
#   file pipeline/s09_residents.py, line 129
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Historic cartography
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

BUILDING_ARTICLES = {}


def mark_buildings(wt):
    """Links to building articles become ⟦title⟧ markers, so a sentence can point at a building by name
    (the Rembrandthuis) as well as by address."""
    def repl(m):
        title = m.group(1).strip()
        title = title[:1].upper() + title[1:]
        text = m.group(2) or m.group(1)
        return f"⟦{title}⟧{text}" if title in BUILDING_ARTICLES else m.group(0)
    return re.sub(r"\[\[([^|\]#]+)(?:\|([^\]]*))?\]\]", repl, wt)
