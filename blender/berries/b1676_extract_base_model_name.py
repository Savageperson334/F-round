# extract_base_model_name
#
# Copied verbatim from https://github.com/earthspecies/avex
#   file scripts/icassp/plot_layer_weights.py, line 20
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def extract_base_model_name(full_name: str) -> str:
    """Extract base model name by removing probe type and layer suffixes.

    Returns
    -------
    str
        The base model name with suffixes removed.
    """
    # Remove common suffixes: _attention_last, _attention_all, _linear_last, _linear_all
    suffixes_to_remove = [
        "_attention_last",
        "_attention_all",
        "_linear_last",
        "_linear_all",
    ]
    base_name = full_name
    for suffix in suffixes_to_remove:
        if base_name.endswith(suffix):
            base_name = base_name[: -len(suffix)]
            break
    return base_name
