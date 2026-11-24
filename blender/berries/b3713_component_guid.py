# component_guid
#
# Copied verbatim from https://github.com/syxscott/PaleoAST
#   file packaging/harvest_payload.py, line 69
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Fossil measurements and paleontology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import hashlib


def component_guid(name: str) -> str:
    """A deterministic GUID so the same file keeps the same component.

    WiX can auto-generate one, but it does that per *build*, and an auto GUID
    that changes on upgrade makes Windows Installer treat the new component as
    a different one -- which is how a 361 MB reinstall ends up as two copies.
    """
    digest = hashlib.sha256(name.encode("utf-8")).hexdigest().upper()
    return f"{{{digest[0:8]}-{digest[8:12]}-{digest[12:16]}-{digest[16:20]}-{digest[20:32]}}}"
