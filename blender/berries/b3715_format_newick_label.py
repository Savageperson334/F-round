# format_newick_label
#
# Copied verbatim from https://github.com/syxscott/PaleoAST
#   file phylogenetics/tree.py, line 61
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Fossil measurements and paleontology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

NEWICK_UNSAFE_CHARS = frozenset(",;:()[]'\"\\ \t\n\r")


def format_newick_label(name: str) -> str:
    """
    Return a Newick-safe representation of ``name``.

    Labels containing Newick structural characters (``, ; : ( ) [ ] '``), a
    backslash or whitespace are wrapped in single quotes with embedded
    apostrophes doubled (``''``), the standard escaping convention.  Plain
    labels are returned unchanged so that numeric internal-node support
    values keep their conventional unquoted form.

    Parameters:
        name: Node label (may be empty or ``None``).

    Returns:
        Label ready for embedding in a Newick string.
    """
    if not name:
        return ""
    if set(name) & NEWICK_UNSAFE_CHARS:
        return "'" + name.replace("'", "''") + "'"
    return name
