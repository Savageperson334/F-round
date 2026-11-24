# output_template
#
# Copied verbatim from https://github.com/Scottcjn/naturelm-cats
#   file NatureLM/infer.py, line 42
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def output_template(model_output: str, start_time: float, end_time: float) -> str:
    """Format the output of the model."""
    return f"#{start_time:.2f}s - {end_time:.2f}s#: {model_output}\n"
