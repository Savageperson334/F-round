# normalize_mac
#
# Copied verbatim from https://github.com/Pouzor/homelable
#   file backend/app/services/mac_utils.py, line 21
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

_OCTET = re.compile(r"[0-9a-f]{1,2}")


def normalize_mac(mac: str | None) -> str | None:
    """Canonical MAC: lowercase, ``-`` → ``:``, stripped, octets zero-padded.

    Blank/None → None. Anything that is not six colon-separated hex octets is
    returned lowercased but otherwise as given, rather than guessed at.
    """
    if not mac:
        return None
    normalized = mac.strip().lower().replace("-", ":")
    octets = normalized.split(":")
    if len(octets) == 6 and all(_OCTET.fullmatch(o) for o in octets):
        return ":".join(o.zfill(2) for o in octets)
    return normalized or None
