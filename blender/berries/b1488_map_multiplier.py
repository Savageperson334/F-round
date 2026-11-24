# map_multiplier
#
# Copied verbatim from https://github.com/cognitivegears/ha-escpos-thermal-printer
#   file custom_components/escpos_printer/printer/mapping_utils.py, line 24
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Thermal printers and obsolete output
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def map_multiplier(val: str | int | None) -> int:
    """Map multiplier string or int to escpos multiplier value (1-8).

    Accepts named sizes ("normal", "double", "triple") or numeric values
    (int or numeric string). Values are clamped to the 1-8 range supported
    by python-escpos custom_size.
    """
    if val is None:
        return 1
    # Accept raw int (e.g. from YAML: width: 4)
    if isinstance(val, int):
        return max(1, min(8, val))
    mapping = {"normal": 1, "double": 2, "triple": 3}
    named = mapping.get(str(val).lower())
    if named is not None:
        return named
    # Accept numeric strings (e.g. "4")
    try:
        return max(1, min(8, int(val)))
    except ValueError, TypeError:
        return 1
