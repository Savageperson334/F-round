# wid
#
# Copied verbatim from https://github.com/syxscott/PaleoAST
#   file packaging/harvest_payload.py, line 37
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Fossil measurements and paleontology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import hashlib
import re

ID_ALLOWED = re.compile(r"[^A-Za-z0-9_.]")


def wid(path: str) -> str:
    """A unique, legal File identifier.

    Sanitising alone is not enough: "GMT" and "GMT+0" both become "GMT_0",
    and "GMT+1" and "GMT+10" differ only by a digit, so the payload contains
    several collisions that light reports as LGHT0091 Duplicate symbol. A short
    hash of the original path keeps the readable prefix for humans and makes
    the id unique for WiX.
    """
    digest = hashlib.sha1(path.encode("utf-8")).hexdigest()[:8]
    cleaned = ID_ALLOWED.sub("_", path)
    if not cleaned or not (cleaned[0].isalpha() or cleaned[0] == "_"):
        cleaned = "_" + cleaned
    # 72 characters is WiX's standard identifier length; stay well under it.
    prefix = cleaned[:60]
    return f"f_{prefix}_{digest}"
