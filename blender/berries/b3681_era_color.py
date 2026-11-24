# era_color
#
# Copied verbatim from https://github.com/strangeloopcanon/paleontology_analytics
#   file blog_assets/make_charts.py, line 46
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Fossil measurements and paleontology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

COLOR_CENO = "#1F5F8B"

COLOR_MESO = "#C0392B"

COLOR_PALEO = "#2E7D5B"


def era_color(time_bin: float) -> str:
    if time_bin > 252:
        return COLOR_PALEO
    if time_bin > 66:
        return COLOR_MESO
    return COLOR_CENO
