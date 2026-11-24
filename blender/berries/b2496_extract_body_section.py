# extract_body_section
#
# Copied verbatim from https://github.com/kcsapp/pygrowl
#   file src/growl/tools/parse_compas_options.py, line 185
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Fossil measurements and paleontology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def extract_body_section(full_text: str) -> str:
    """
    Return only the portion of the document that contains individual option
    entries (i.e. the "COMPAS information" and "Alphabetical listing" sections),
    excluding the trailing "Category listing" section, which just lists option
    names without descriptions and would otherwise produce bogus/duplicate entries.
    """
    start_marker = "COMPAS information"
    end_marker = "Category listing"

    start = full_text.find(start_marker)
    end = full_text.find(end_marker, start if start != -1 else 0)

    if start == -1:
        start = 0
    if end == -1:
        end = len(full_text)

    return full_text[start:end]
