# scene_digest
#
# Copied verbatim from https://github.com/ymatterlab/ycrystal
#   file src/ycrystal/render/thumbnails.py, line 153
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import hashlib


def scene_digest(text: str) -> str:
    """Return a SHA-256 digest of a scene, ignoring comment lines.

    Comments carry the generation time, the Ycrystal version, and descriptions, which do
    not change the image.
    """
    content = "\n".join(
        line for line in text.splitlines() if line.strip() and not line.lstrip().startswith("//")
    )
    return hashlib.sha256(content.encode("utf-8")).hexdigest()
