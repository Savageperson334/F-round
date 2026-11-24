# remove_matching_braces
#
# Copied verbatim from https://github.com/MartinThoma/hwrt
#   file hwrt/datasets/mathbrush.py, line 50
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def remove_matching_braces(latex):
    """
    If `latex` is surrounded by matching braces, remove them. They are not
    necessary.

    Parameters
    ----------
    latex : string

    Returns
    -------
    string

    Examples
    --------
    >>> remove_matching_braces('{2+2}')
    '2+2'
    >>> remove_matching_braces('{2+2')
    '{2+2'
    """
    if latex.startswith("{") and latex.endswith("}"):
        opened = 1
        matches = True
        for char in latex[1:-1]:
            if char == "{":
                opened += 1
            elif char == "}":
                opened -= 1
            if opened == 0:
                matches = False
        if matches:
            latex = latex[1:-1]
    return latex
