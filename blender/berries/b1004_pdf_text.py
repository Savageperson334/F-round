# pdf_text
#
# Copied verbatim from https://github.com/alepersichetti/WyrmHex
#   file wyrmhex.py, line 5298
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Cave surveys and subterranean maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def pdf_text(text):
    """The PDF uses the fonts built into every PDF reader, which only know
    Latin-1 (enough for Italian): anything else gets its nearest ASCII."""
    for fancy, plain in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("—", "-"), ("–", "-"), ("…", "...")):
        text = text.replace(fancy, plain)
    return text.encode("latin-1", "replace").decode("latin-1")
