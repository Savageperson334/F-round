# reorder_legend_keys
#
# Copied verbatim from https://github.com/Augtumn/IsoLeadToolkit
#   file ui/main_window_parts/legend_entries.py, line 31
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def reorder_legend_keys(
    order_keys: list[str],
    src_full: str,
    target_full: str,
    below: bool,
) -> list[str]:
    """Return the reordered ``legend_item_order`` list after a drag.

    *src_full* is moved to the position of *target_full* (before it, or
    after it when *below*). Rows are identified by their full
    ``type:key`` order keys. No-op when either key is unknown.
    """
    order = list(order_keys)
    if src_full not in order or target_full not in order or src_full == target_full:
        return order
    order.remove(src_full)
    idx = order.index(target_full)
    if below:
        idx += 1
    order.insert(idx, src_full)
    return order
