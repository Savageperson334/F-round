# eta_squared
#
# Copied verbatim from https://github.com/syxscott/PaleoAST
#   file stats/univariate.py, line 1086
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Fossil measurements and paleontology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def eta_squared(F_statistic: float, df_between: int, df_within: int) -> float:
    """
    Compute partial eta-squared (η²) from ANOVA results.

    η² represents the proportion of variance in the dependent variable
    that is explained by the independent variable.

    Formula (Cohen 1988, eq. 8.2.3):
        η² = (F * df_between) / (F * df_between + df_within)

    Parameters
    ----------
    F_statistic : float
        Observed F-statistic from ANOVA.
    df_between : int
        Degrees of freedom between groups.
    df_within : int
        Degrees of freedom within groups (error df).

    Returns
    -------
    float
        Partial eta-squared (bounded [0, 1]).

    Raises
    ------
    ValueError
        If df_between <= 0 or df_within < 0.

    Notes
    -----
    Interpretation guidelines (Cohen 1988):
        η² ≈ 0.01  -> small
        η² ≈ 0.06  -> medium
        η² ≈ 0.14  -> large

    Warning: η² is a biased overestimate of the true effect size,
    especially for small samples. Consider using omega-squared (ω²)
    for more accurate estimates.

    References
    ----------
    Cohen, J. (1988). *Statistical Power Analysis for the Behavioral
    Sciences* (2nd ed.). Lawrence Erlbaum Associates.
    Lakens, D. (2013). Calculating and reporting effect sizes to
    facilitate cumulative science. *Frontiers in Psychology*, 4, 863.
    """
    if df_between <= 0:
        raise ValueError("df_between must be a positive integer")
    if df_within < 0:
        raise ValueError("df_within must be a non-negative integer")

    numerator = F_statistic * df_between
    denominator = numerator + df_within

    if denominator == 0.0:
        return 0.0

    eta2 = numerator / denominator

    # Bound to [0, 1] for numerical stability
    return float(np.clip(eta2, 0.0, 1.0))
