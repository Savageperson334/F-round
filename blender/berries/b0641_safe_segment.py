# safe_segment
#
# Copied verbatim from https://github.com/Pouzor/homelable
#   file backend/app/services/doc_export.py, line 49
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

_UNSAFE = re.compile(r"[^a-z0-9._-]+")


def safe_segment(raw: str) -> str:
    """One path segment that cannot escape the archive or collide with a device.

    Slugs come from `slugify` and are already tame, but a body can be exported
    long after a title was renamed by hand, and `..` or a leading dot would be a
    zip-slip waiting for whichever tool unpacks this.
    """
    cleaned = _UNSAFE.sub("-", (raw or "").strip().lower()).strip("-.")
    return cleaned or "untitled"
