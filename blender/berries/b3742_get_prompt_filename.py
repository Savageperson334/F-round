# get_prompt_filename
#
# Copied verbatim from https://github.com/thecrazymage/CasTex
#   file src/prompt_processing.py, line 6
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Textures and materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_prompt_filename(prompt, directional=True):
    """Generates a standardized filename for caching text embeddings based on the prompt content."""
    if directional:
        return f'directional_embeddings_{prompt.replace(" ", "_")}.pt'
    else:
        return f'embeddings_{prompt.replace(" ", "_")}.pt'
