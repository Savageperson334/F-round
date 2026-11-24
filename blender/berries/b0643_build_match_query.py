# build_match_query
#
# Copied verbatim from https://github.com/Pouzor/homelable
#   file backend/app/services/doc_search.py, line 121
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def build_match_query(raw: str) -> str:
    """Turn user input into an FTS5 MATCH expression.

    Every term is quoted, so punctuation a user types (`192.168.1.1`, `nas-01`,
    an unbalanced quote) is data rather than FTS5 syntax, and gets a prefix `*`
    so typing half a word still matches.
    """
    terms = [term.replace('"', '""') for term in raw.split() if term.strip()]
    return " AND ".join(f'"{term}"*' for term in terms)
