# classify_status
#
# Copied verbatim from https://github.com/ItIsMixian/Orrery
#   file scripts/docsite/build_docsite.py, line 119
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def classify_status(val: str):
    v = val.strip().lower()
    if v.startswith("superseded"):
        return ("Superseded", "superseded")
    if v.startswith("deprecated"):
        return ("Deprecated", "deprecated")
    if v.startswith("proposed"):
        return ("Proposed", "proposed")
    if v.startswith("design"):
        return ("Design / Deferred", "deferred")
    if v.startswith("accepted"):
        if "superseded" in v:
            return ("Accepted → Superseded", "superseded")
        return ("Accepted", "accepted")
    cleaned = re.sub(r"[（(].*", "", val).strip()
    return (cleaned[:28] or "Unknown", "other")
