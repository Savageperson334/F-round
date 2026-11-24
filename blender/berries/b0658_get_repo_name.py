# get_repo_name
#
# Copied verbatim from https://github.com/R2E-Gym/R2E-Gym
#   file src/r2egym/swesmith/utils.py, line 21
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_repo_name(repo, commit) -> str:
    """
    Get the SWE-smith GitHub repository name for a repository at a specific commit.
    """
    return f"{repo.replace('/', '__')}.{commit[:8]}"
