# normalise_sku
#
# Copied verbatim from https://github.com/AkshayTallikar/software-archaeology
#   file modern_app/main.py, line 209
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def normalise_sku(raw: str | None) -> str | None:
    """Canonical SKU, or None when missing or blank.

    Evidence: sku is case-insensitive and whitespace-trimmed (widget, ' Widget ',
    'GADGET  ' all price as the catalogue entry).
    """
    if raw is None or not raw.strip():
        return None
    return raw.strip().upper()
