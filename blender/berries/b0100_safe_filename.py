# safe_filename
#
# Copied verbatim from https://github.com/BAHALLA/orrery
#   file core/orrery_core/serving/attachments.py, line 219
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import unicodedata
import re

_UNSAFE_NAME_CHARS = re.compile(r"[^\w.\- ()]+")


def safe_filename(raw: str) -> str:
    """An inert label for a client-supplied file name.

    The model reads it inside the placeholder, so it must not be able to carry
    instructions or forge a second placeholder: no path, no control or
    bracket characters, and short.
    """
    name = unicodedata.normalize("NFKC", raw or "")
    name = name.replace("\\", "/").rsplit("/", 1)[-1]
    name = "".join(ch for ch in name if unicodedata.category(ch)[0] != "C")
    name = _UNSAFE_NAME_CHARS.sub("_", name).strip(" .")
    if len(name) > 80:
        stem, dot, ext = name.rpartition(".")
        name = f"{stem[: 80 - len(ext) - 2]}…{dot}{ext}" if dot and len(ext) <= 10 else name[:80]
    return name or "upload"
