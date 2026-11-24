# observation_factor
#
# Copied verbatim from https://github.com/lmizrahi/etas
#   file etas/inversion.py, line 663
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def observation_factor(beta, delta_mc):
    """Number of events above ``m_ref`` per event observed above
    ``mc_current``.

    ``1 + zeta = exp(beta * delta_mc)``, from the Gutenberg-Richter law
    (Mizrahi et al. 2021, JGR, Sect. 3.1).

    Parameters
    ----------
    beta : float
        Gutenberg-Richter parameter (natural-log units).
    delta_mc : float or array-like
        Completeness above the reference magnitude,
        ``mc_current - m_ref``.

    Returns
    -------
    float or array-like
    """
    zeta_plus_1 = np.exp(beta * delta_mc)
    return zeta_plus_1
