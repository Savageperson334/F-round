# bateman
#
# Copied verbatim from https://github.com/timpol/pysoplot
#   file src/pysoplot/ludwig.py, line 115
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def bateman(Lam, series='238U'):
    """
    Return Bateman coefficients for the 238U or 235U decay series as defined in
    Ludwig (1977).

    Parameters
    -----------
    Lam : array-like
        array of relevant decay constants (see below)
    series : {'238U', '235U'}, optional
        Uranium series to compute coefficients for.

    References
    -----------
    Ludwig, K.R., 1977. Effect of initial radioactive-daughter disequilibrium
    on U-Pb isotope apparent ages of young minerals. Journal of Research of
    the US Geological Survey 5, 663–667.

    """
    assert series in ('238U', '235U')

    if series == '238U':

        # Lam[0] = lam238
        # Lam[1] = lam234
        # Lam[2] = lam230
        # Lam[3] = lam226
        # Lam[4] = lam210 <- not currently used

        # ignoring 210Pb
        c1 = -Lam[1]*Lam[2]*Lam[3] / ((Lam[1]-Lam[0]) * (Lam[2]-Lam[0]) * (Lam[3]-Lam[0]))
        c2 = -Lam[0]*Lam[2]*Lam[3] / ((Lam[0]-Lam[1]) * (Lam[2]-Lam[1]) * (Lam[3]-Lam[1]))
        c3 = -Lam[0]*Lam[1]*Lam[3] / ((Lam[0]-Lam[2]) * (Lam[1]-Lam[2]) * (Lam[3]-Lam[2]))
        c4 = -Lam[0]*Lam[1]*Lam[2] / ((Lam[0]-Lam[3]) * (Lam[1]-Lam[3]) * (Lam[2]-Lam[3]))

        h1 = -Lam[2]*Lam[3] / ((Lam[2]-Lam[1]) * (Lam[3]-Lam[1]))
        h2 = -Lam[1]*Lam[3] / ((Lam[1]-Lam[2]) * (Lam[3]-Lam[2]))
        h3 = -Lam[1]*Lam[2] / ((Lam[1]-Lam[3]) * (Lam[2]-Lam[3]))

        p1 = -Lam[3] / (Lam[3]-Lam[2])
        p2 = -Lam[2] / (Lam[2]-Lam[3])

        return np.array((c1, c2, c3, c4, h1, h2, h3, p1, p2))

    else:
        # Lam[0] = lam235
        # Lam[1] = lam231
        # Lam[2] = lam227 <- not currently used

        # ignoring 227Ac
        d1 = -Lam[1] / (Lam[1]-Lam[0])
        d2 = -Lam[0] / (Lam[0]-Lam[1])

        return np.array((d1, d2))
