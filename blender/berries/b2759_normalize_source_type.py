# normalize_source_type
#
# Copied verbatim from https://github.com/microsoft/haste
#   file hastelib/src/hastegeo/core/utils/source_types.py, line 23
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

LEGACY_SOURCE_TYPE_ALIASES = {
    "maxar": "vantor",
}


def normalize_source_type(source_type):
    """Return the canonical, lower-cased key for ``source_type``.

    Args:
        source_type: A source-type key, e.g. ``"vantor"`` or the
            pre-rebrand ``"maxar"``. Non-string values (including
            ``None``) are returned unchanged so callers can pass an
            optional field straight through without a guard.

    Returns:
        The canonical key, lower-cased and stripped; unknown keys are
        passed through unchanged (aside from case/whitespace) so this
        never silently discards a value it does not recognize.
    """
    if not isinstance(source_type, str):
        return source_type
    key = source_type.strip().lower()
    return LEGACY_SOURCE_TYPE_ALIASES.get(key, key)
