# safe_cache_slug
#
# Copied verbatim from https://github.com/JonnyCarter/Delivery-Archaeology
#   file src/delivery_archaeology/storage.py, line 7
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import hashlib
import re


def safe_cache_slug(value: str) -> str:
    text = value.strip()
    slug = re.sub(r"[^A-Za-z0-9_-]+", "-", text).strip("-_")
    slug = slug[:80] or "value"
    if slug == text:
        return slug
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()[:8]
    return f"{slug}-{digest}"
