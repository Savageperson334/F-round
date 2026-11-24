# getBestCandidateCoord
#
# Copied verbatim from https://github.com/anopara/texture-synthesis-nonparametric-sampling
#   file textureSynthesis.py, line 123
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Textures and materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import floor
import numpy as np


def getBestCandidateCoord(bestCandidateMap, outputSize):

    candidate_row = floor(np.argmax(bestCandidateMap) / outputSize[0])
    candidate_col = np.argmax(bestCandidateMap) - candidate_row * outputSize[1]

    return candidate_row, candidate_col
