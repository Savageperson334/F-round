# normalize_host
#
# Copied verbatim from https://github.com/Pouzor/homelable
#   file backend/app/core/config.py, line 520
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def normalize_host(host: str) -> str:
    """Compare-ready host: trimmed, no trailing dot, lowercase."""
    return host.strip().rstrip(".").lower()
