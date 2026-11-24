# extract_issue
#
# Copied verbatim from https://github.com/R2E-Gym/R2E-Gym
#   file src/r2egym/repo_analysis/build_syn_issue.py, line 12
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def extract_issue(model_output: str):
    if "[ISSUE]" in model_output:
        model_output = model_output.split("[ISSUE]")[1]
    return model_output.split("[/ISSUE]")[0].strip()
