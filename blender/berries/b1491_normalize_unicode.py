# normalize_unicode
#
# Copied verbatim from https://github.com/cognitivegears/ha-escpos-thermal-printer
#   file custom_components/escpos_printer/text_utils/transcoding.py, line 37
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Thermal printers and obsolete output
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import unicodedata


def normalize_unicode(text: str) -> str:
    """Normalize Unicode text using NFKC normalization.

    NFKC normalization converts compatibility characters to their canonical
    equivalents (e.g., ligatures to separate characters, full-width to half-width).

    Args:
        text: Unicode text to normalize.

    Returns:
        Normalized text.
    """
    return unicodedata.normalize("NFKC", text)
