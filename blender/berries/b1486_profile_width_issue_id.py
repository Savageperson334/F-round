# profile_width_issue_id
#
# Copied verbatim from https://github.com/cognitivegears/ha-escpos-thermal-printer
#   file custom_components/escpos_printer/printer/base_adapter.py, line 83
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Thermal printers and obsolete output
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def profile_width_issue_id(entry_id: str | None) -> str:
    """Build the per-entry repair-issue id for the profile-width fallback.

    Scoped by ``entry_id`` (rather than profile name) so two entries
    configured with the same profile don't share — and clobber — the same
    issue. Also used by ``async_remove_entry`` to clean up on entry
    removal.
    """
    return f"profile_width_fallback_{entry_id or 'unknown'}"
