# chunks_to_string
#
# Copied verbatim from https://github.com/MartinThoma/hwrt
#   file hwrt/latex.py, line 103
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def chunks_to_string(chunks):
    """
    Parameters
    ----------
    chunks : list of strings
        A list of single entities in order

    Returns
    -------
    string :
        A LaTeX-parsable string

    Examples
    --------
    >>> chunks_to_string(['\\\\sum', '_', 'i', '^', 'n', 'i', '^', '2'])
    '\\\\sum_{i}^{n}i^{2}'
    >>> chunks_to_string(['\\\\sum', '_', '{', 'i', '}', '^', 'n', 'i', '^',
    ...                   '2'])
    '\\\\sum_{i}^{n}i^{2}'
    """
    string = ""
    began_context = False
    context_depth = 0
    context_triggers = ["_", "^"]
    for chunk in chunks:
        if began_context and chunk != "{":
            string += "{" + chunk + "}"
            began_context = False
        elif began_context and chunk == "{":
            began_context = False
            string += chunk
        else:
            if chunk in context_triggers:
                began_context = True
                context_depth += 1
            string += chunk
    return string
