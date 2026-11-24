# filter_label
#
# Copied verbatim from https://github.com/MartinThoma/hwrt
#   file hwrt/analyze_data.py, line 23
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def filter_label(label, replace_by_similar=True):
    """Some labels currently don't work together because of LaTeX naming
    clashes. Those will be replaced by simple strings."""
    bad_names = [
        "celsius",
        "degree",
        "ohm",
        "venus",
        "mars",
        "astrosun",
        "fullmoon",
        "leftmoon",
        "female",
        "male",
        "checked",
        "diameter",
        "sun",
        "Bowtie",
        "sqrt",
        "cong",
        "copyright",
        "dag",
        "parr",
        "notin",
        "dotsc",
        "mathds",
        "mathfrak",
    ]
    if any(label[1:].startswith(bad) for bad in bad_names):
        if label == "\\dag" and replace_by_similar:
            return "\\dagger"
        elif label == "\\diameter" and replace_by_similar:
            return "\\O"
        return label[1:]
    else:
        return label
