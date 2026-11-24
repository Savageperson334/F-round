# esc
#
# Copied verbatim from https://github.com/syxscott/PaleoAST
#   file packaging/harvest_payload.py, line 62
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Fossil measurements and paleontology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def esc(text) -> str:
    """XML-escape. The build tree lives under 'D:\\Program Files\\...', so the
    ampersand is not hypothetical -- and it has to be replaced first, or it
    turns the escapes of the other two into entities of their own."""
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
