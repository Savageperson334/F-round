# normalize_paths
#
# Copied verbatim from https://github.com/R2E-Gym/R2E-Gym
#   file src/r2egym/agenthub/utils/utils.py, line 311
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def normalize_paths(file_list):
    """Normalize file paths by removing leading slashes or other differences."""
    return [file.lstrip("./") for file in file_list]
