# decolor_dict_keys
#
# Copied verbatim from https://github.com/R2E-Gym/R2E-Gym
#   file src/r2egym/repo_analysis/execution_log_parser.py, line 68
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def decolor_dict_keys(key):
    decolor = lambda key: re.sub(r"\u001b\[\d+m", "", key)
    return {decolor(k): v for k, v in key.items()}
