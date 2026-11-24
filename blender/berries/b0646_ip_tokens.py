# ip_tokens
#
# Copied verbatim from https://github.com/Pouzor/homelable
#   file backend/app/services/inventory_sync.py, line 57
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def ip_tokens(ip: str | None) -> list[str]:
    """Split an ``ip`` field into individual addresses.

    A node or device may carry several comma-separated addresses — a router with
    a management VLAN, a host behind a VIP — so identity matching compares per
    token rather than on the whole string. Every matcher that resolves a device
    from addresses shares this rule, the scanner included.
    """
    return [t.strip() for t in ip.split(",") if t.strip()] if ip else []
