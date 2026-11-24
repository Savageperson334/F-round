# format_hex
#
# Copied verbatim from https://github.com/touchbr/Graphite
#   file scripts/soften_colormap.py, line 170
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def clamp(value: float, minimum: float, maximum: float) -> float:
    return min(max(value, minimum), maximum)


def format_hex(red: float, green: float, blue: float, alpha: str | None) -> str:
    rgb = (
        round(clamp(red, 0, 1) * 255),
        round(clamp(green, 0, 1) * 255),
        round(clamp(blue, 0, 1) * 255),
    )
    suffix = alpha or ""
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}{suffix}"
