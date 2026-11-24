# view_key_port
#
# Copied verbatim from https://github.com/Pouzor/homelable
#   file backend/app/services/inventory_sync.py, line 304
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def view_key_port(key: str) -> str:
    """``key`` reduced to the port it names, the form a pre-#503 view stored.

    What a view addresses can move: editing a service's host or path in the
    Device Inventory rewrites its key, and the canvases drawing it still hold
    the old one. Both spell the same port, so that is what they are matched on
    once the exact key misses. A port-less service has no such form — its name
    is all it has — and keeps its key.
    """
    parts = key.split("|")
    if len(parts) < 2 or parts[0] in ("", "None"):
        return key
    return f"{parts[0]}|{parts[1]}"
