# clean_text
#
# Copied verbatim from https://github.com/gvard/astrodata
#   file src/astrodata/solarsystem/mk_data_json_from_html_solsys.py, line 12
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def clean_text(text: str) -> str:
    """Helper function to clear special characters."""
    if not text:
        return ""
    return (
        text.replace("\u0160", "S")
        .replace("\u2013", "-")
        .replace("á", "a")
        .replace("ʻ", "'")
        .replace("\xa0", "")
        .strip()
    )
