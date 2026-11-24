# omega_squared
#
# Copied verbatim from https://github.com/syxscott/PaleoAST
#   file stats/univariate.py, line 1150
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Fossil measurements and paleontology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def omega_squared(F_statistic: float, df_between: int, df_within: int, n: int) -> float:
    """
    Compute omega-squared (ω²) from ANOVA results.

    ω² is a less biased alternative to η² that better estimates the
    population effect size, especially for small samples.

    Formula (Cohen 1988, eq. 8.2.4; adapted from Lakens 2013):
        ω² = (F*df_between - df_between) / (F*df_between + df_within + 1)

    Parameters
    ----------
    F_statistic : float
        Observed F-statistic from ANOVA.
    df_between : int
        Degrees of freedom between groups.
    df_within : int
        Degrees of freedom within groups (error df).
    n : int
        Total number of observations.

    Returns
    -------
    float
        Omega-squared (bounded [0, 1]).

    Raises
    ------
    ValueError
        If df_between <= 0, df_within < 0, or n <= df_between.

    Notes
    -----
    Interpretation guidelines (Cohen 1988):
        ω² ≈ 0.01  -> small
        ω² ≈ 0.06  -> medium
        ω² ≈ 0.14  -> large

    ω² is generally preferred over η² because it provides a less
    biased estimate of the population effect size.

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
    if n <= df_between:
        raise ValueError(f"Total observations n ({n}) must exceed df_between ({df_between})")

    numerator = F_statistic * df_between - df_between
    denominator = F_statistic * df_between + df_within + 1.0

    if denominator == 0.0:
        return 0.0

    omega2 = numerator / denominator

    return float(np.clip(omega2, 0.0, 1.0))
