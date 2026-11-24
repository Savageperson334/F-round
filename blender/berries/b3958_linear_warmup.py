# linear_warmup
#
# Copied verbatim from https://github.com/xandergos/terrain-diffusion
#   file terrain_diffusion/training/trainers/gan.py, line 15
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def linear_warmup(start_value, end_value, current_step, total_steps):
    """Perform linear warmup from start_value to end_value."""
    if current_step >= total_steps:
        return end_value
    return start_value + (end_value - start_value) * (current_step / total_steps)
