# decide
#
# Copied verbatim from https://github.com/Pouzor/homelable
#   file backend/app/services/doc_reconcile.py, line 379
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

AUTO = "auto"

CONFLICT = "conflict"

SAME = "same"


def decide(cur: str | None, old: str | None, new: str | None) -> str:
    """Classify one fact or section given its current, baseline and device value.

    The rules, in order:

    * the user already has the device's value → nothing to do;
    * the device is unchanged → nothing to do, whatever the user wrote;
    * an untouched, baseline-backed value follows a device removal;
    * a device removal whose current value differs from the baseline → ask;
    * no baseline for it and nothing in the document → safe to add;
    * no baseline for it and the document differs → ask (conservative);
    * the user left the baseline value → safe to apply;
    * anything else → the user touched it and the device changed it: conflict.
    """
    if cur == new:
        return SAME
    if old == new:
        return SAME
    if old is not None and cur == old:
        return AUTO
    if not new:
        return CONFLICT  # device dropped the value the user still shows
    if old is None:
        return AUTO if not cur else CONFLICT
    return CONFLICT
