# commit_message
#
# Copied verbatim from https://github.com/Pouzor/homelable
#   file backend/app/services/git_sync.py, line 313
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def commit_message(doc_count: int, diagram_count: int) -> str:
    docs = f"{doc_count} document{'s' if doc_count != 1 else ''}"
    diagrams = f"{diagram_count} diagram{'s' if diagram_count != 1 else ''}"
    return f"Homelable sync: {docs}, {diagrams}"
