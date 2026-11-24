# blend
#
# Copied verbatim from https://github.com/c64cryptoboy/retro-archaeology-skills
#   file skills/c64-basic-v2-rnd-analysis/analysis/render_component_depth.py, line 27
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def blend(rgb: tuple[int, int, int], amount: float) -> str:
    base = (23, 34, 44)
    values = tuple(round(base[i] + (rgb[i] - base[i]) * amount) for i in range(3))
    return "#" + "".join(f"{value:02x}" for value in values)
