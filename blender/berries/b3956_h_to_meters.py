# h_to_meters
#
# Copied verbatim from https://github.com/xandergos/terrain-diffusion
#   file terrain_diffusion/inference/utils/azgaar_to_tiff.py, line 87
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def h_to_meters(h, exponent, ocean_max_depth=4000.0, ocean_power=1.5):
    """Convert Azgaar internal height (0-100) to meters.

    Land (h >= 20) matches Azgaar's getHeight(): (h-18)^exponent
    Ocean (h < 20) uses a power curve: -ocean_max_depth * ((20-h)/20)^ocean_power
      h=0  -> -ocean_max_depth (deepest ocean)
      h=19 -> ~-45 m at defaults (coastal shelf)
    """
    if h < 20:
        return -ocean_max_depth * ((20 - h) / 20) ** ocean_power
    return float(h - 18) ** exponent
