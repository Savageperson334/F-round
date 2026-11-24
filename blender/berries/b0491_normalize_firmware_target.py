# normalize_firmware_target
#
# Copied verbatim from https://github.com/MacNite/HiveHub
#   file server/schemas.py, line 669
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Beehives and unusual agriculture
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

FIRMWARE_TARGET_ALIASES = {"hivehub": "hivescale"}


def normalize_firmware_target(target: str) -> str:
    """Map a user-supplied OTA target onto its canonical stored value.

    Folds the "hivehub" alias onto "hivescale" (and lower-cases / trims). Unknown
    values pass through unchanged so the usual target validation still rejects them.
    """
    t = (target or "").strip().lower()
    return FIRMWARE_TARGET_ALIASES.get(t, t)
