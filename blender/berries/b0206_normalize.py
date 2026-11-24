# normalize
#
# Copied verbatim from https://github.com/Evolving-AI-Lab/synthesizing
#   file patchShow.py, line 3
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def normalize(img, out_range=(0.,1.), in_range=None):
  if not in_range:
    min_val = np.min(img)
    max_val = np.max(img)
  else:
    min_val = in_range[0]
    max_val = in_range[1]
  result = np.copy(img)
  result[result > max_val] = max_val
  result[result < min_val] = min_val
  result = (result - min_val) / (max_val - min_val) * (out_range[1] - out_range[0]) + out_range[0]
  return result
