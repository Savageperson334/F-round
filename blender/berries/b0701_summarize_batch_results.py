# summarize_batch_results
#
# Copied verbatim from https://github.com/Scottcjn/naturelm-cats
#   file inference_web_app.py, line 134
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from collections import Counter


def summarize_batch_results(results):
    summary = Counter(results)
    summary_str = "\n".join(f"{k}: {v}" for k, v in summary.most_common())
    return summary_str
