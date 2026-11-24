# g
#
# Copied verbatim from https://github.com/timpol/pysoplot
#   file src/pysoplot/wendt_carl.py, line 44
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def g(t, A15i, DC):
    """
    207Pb/235U atomic ratio as a function of time and actvitiy
    ratios using equation from [Wendt1985]_.

    References
    ----------
    .. [Wendt1985] Wendt, I., Carl, C., 1985. U/Pb dating of discordant 0.1
       Ma old secondary U minerals. Earth and Planetary Science Letters 73, 278–284.
    """
    D0 = A15i - 1.
    f1 = np.exp(DC[0] * t) - 1 + D0 * (DC[0] / DC[1]) * np.exp(DC[0] * t) \
         * (1 - np.exp(-DC[1] * t))
    return f1
