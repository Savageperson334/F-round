# slugify
#
# Copied verbatim from https://github.com/Pouzor/homelable
#   file backend/app/services/doc_tree.py, line 41
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

_SLUG_STRIP = re.compile(r"[^a-z0-9]+")


def slugify(title: str) -> str:
    slug = _SLUG_STRIP.sub("-", (title or "").strip().lower()).strip("-")
    return slug[:80] or "untitled"
