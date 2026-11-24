# levenshteinDistanceDP
#
# Copied verbatim from https://github.com/jackson-waschura/bioacoustic-detection
#   file src/bioacoustic_detection/utils/annot.py, line 146
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Ocean hydrophones and acoustic ecology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def levenshteinDistanceDP(token1, token2):
    """
    Efficiently calculates the Levenshtein distance (edit distance) between two
    strings. Useful for determining if a column name has been misspelled.

    The cost of insertions, deletions, and substitutions are all set to 1.

    Parameters
    token1 : str
        first token
    token2 : str
        second token

    Returns
    distance : int
        the number of single-character edits required to turn token1 into token2
    """

    distances = np.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    a, b, c = 0, 0, 0

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1-1] == token2[t2-1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]

                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    return distances[len(token1)][len(token2)]
