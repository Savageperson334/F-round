# clamp_validation_sample
#
# Copied verbatim from https://github.com/microsoft/haste
#   file hastelib/src/hastegeo/core/utils/validation_config.py, line 56
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

MAX_VALIDATION_SAMPLE = 2000

MIN_VALIDATION_SAMPLE = 1


def clamp_validation_sample(sample_size: int) -> int:
    """Clamp a requested sample size to the supported range."""
    return max(
        MIN_VALIDATION_SAMPLE,
        min(int(sample_size), MAX_VALIDATION_SAMPLE),
    )
