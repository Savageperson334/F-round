# dist_to_path
#
# Copied verbatim from https://github.com/ygd551/terra-incognita
#   file tools/tracking_report.py, line 32
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Cave surveys and subterranean maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def dist_to_path(q, P):
    a, b = P[:-1], P[1:]
    ab = b - a
    t = np.clip(np.einsum("ij,ij->i", q - a, ab) / np.maximum(np.einsum("ij,ij->i", ab, ab), 1e-12), 0, 1)
    return np.linalg.norm(a + t[:, None] * ab - q, axis=1).min()
