# mm_to_inch
#
# Copied verbatim from https://github.com/Augtumn/IsoLeadToolkit
#   file application/use_cases/export_image.py, line 198
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def mm_to_inch(mm_value: float) -> float:
    """Convert millimeter to inch."""
    return float(mm_value) / 25.4
