# prod_neg_log_lik
#
# Copied verbatim from https://github.com/lmizrahi/etas
#   file etas/inversion.py, line 1238
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def prod_neg_log_lik(a, args):
    """Objective for estimating ``a`` from individual productivities.

    Absolute value of the derivative with respect to ``a`` of the (weighted)
    Poisson log-likelihood of ``kappa ~ k0 * exp(a * m_diff)``, with ``k0``
    profiled out. Its minimum (zero) is the maximum-likelihood ``a``.

    Parameters
    ----------
    a : float or array of one float
    args : list
        ``[kappa, m_diff, weights]``, see `calc_a_k0_from_kappa`.

    Returns
    -------
    float
    """
    sk, md, weights = args
    k_0 = np.sum(weights * sk) / (weights * np.exp(a * md)).sum()
    ll = (weights * md * (sk - k_0 * np.exp(a * md))).sum()
    return np.abs(ll)
