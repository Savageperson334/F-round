# partial_eta_squared
#
# Copied verbatim from https://github.com/syxscott/PaleoAST
#   file stats/univariate.py, line 1216
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Fossil measurements and paleontology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def partial_eta_squared(F_statistic: float, df_between: int, df_error: int) -> float:
    """
    Compute partial eta-squared (η²_p) from ANOVA results.

    Partial η²_p represents the proportion of variance explained by a
    factor controlling for other factors, commonly used in ANCOVA.

    Formula (Cohen 1992):
        η²_p = (F * df_between) / (F * df_between + df_error)

    Parameters
    ----------
    F_statistic : float
        Observed F-statistic from ANOVA/ANCOVA.
    df_between : int
        Degrees of freedom for the effect (numerator df).
    df_error : int
        Degrees of freedom for the error (denominator df).

    Returns
    -------
    float
        Partial eta-squared (bounded [0, 1]).

    Raises
    ------
    ValueError
        If df_between <= 0 or df_error < 0.

    Notes
    -----
    This function is equivalent to `eta_squared` when there is only
    one factor (no covariates). The distinction is conceptual: partial
    η² is the preferred measure when there are multiple factors or
    covariates.

    References
    ----------
    Cohen, J. (1992). A power primer. *Psychological Bulletin*, 112(1), 155–159.
    Lakens, D. (2013). Calculating and reporting effect sizes to
    facilitate cumulative science. *Frontiers in Psychology*, 4, 863.
    """
    if df_between <= 0:
        raise ValueError("df_between must be a positive integer")
    if df_error < 0:
        raise ValueError("df_error must be a non-negative integer")

    numerator = F_statistic * df_between
    denominator = numerator + df_error

    if denominator == 0.0:
        return 0.0

    eta2p = numerator / denominator

    return float(np.clip(eta2p, 0.0, 1.0))
