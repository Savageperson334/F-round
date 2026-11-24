# cleanup_cut
#
# Copied verbatim from https://github.com/cognitivegears/ha-escpos-thermal-printer
#   file custom_components/escpos_printer/printer/mapping_utils.py, line 61
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Thermal printers and obsolete output
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def cleanup_cut(cut: str | None) -> str:
    """Return the cut mode to use for best-effort cleanup after a failure.

    The normal default ``cut="none"`` means "don't cut" on a *successful*
    print, but on a cancelled/failed print we want to sever the
    half-printed receipt so it doesn't hang into the next job. ``"none"``
    (or empty/None) therefore falls through to a full cut here; an
    explicit ``"partial"``/``"full"`` is honoured as-is.

    (Plain ``cut or "full"`` was wrong because ``DEFAULT_CUT == "none"``
    is truthy, so it was never replaced and ``map_cut("none")`` → no cut.)
    """
    if cut and cut.lower() != "none":
        return cut
    return "full"
