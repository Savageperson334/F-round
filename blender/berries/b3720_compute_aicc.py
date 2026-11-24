# compute_aicc
#
# Copied verbatim from https://github.com/syxscott/PaleoAST
#   file stats/univariate.py, line 880
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Fossil measurements and paleontology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def compute_aicc(log_likelihood: float, n_params: int, n_obs: int) -> float:
    """
    Compute the small-sample corrected Akaike Information Criterion (AICc).

    AICc corrects for finite sample size and is preferred over AIC when
    the sample size is small relative to the number of parameters
    (typically when n / k < 40).

    Formula (Burnham & Anderson 2002, eq. 2.2.2):
        AIC  = -2 * LL + 2 * k
        AICc = AIC + (2 * k * (k + 1)) / (n - k - 1)

    Parameters
    ----------
    log_likelihood : float
        Log-likelihood of the fitted model.
    n_params : int
        Number of estimated parameters (k).
    n_obs : int
        Number of observations (n).

    Returns
    -------
    float
        The AICc value.

    Raises
    ------
    ValueError
        If n - k - 1 <= 0 (insufficient data for correction).

    References
    ----------
    Burnham, K. P., & Anderson, D. R. (2002). *Model Selection and
    Multimodel Inference: A Practical Information-Theoretic Approach*
    (2nd ed.). Springer.
    """
    if n_params <= 0:
        raise ValueError("n_params must be a positive integer")
    if n_obs <= 0:
        raise ValueError("n_obs must be a positive integer")
    if n_params >= n_obs:
        raise ValueError(f"n_params ({n_params}) must be less than n_obs ({n_obs}) for AICc computation")
    if n_obs - n_params - 1 <= 0:
        raise ValueError(f"Insufficient data for AICc correction: n ({n_obs}) - k ({n_params}) - 1 must be > 0")

    k = n_params
    n = n_obs
    aic = -2.0 * log_likelihood + 2.0 * k
    correction = (2.0 * k * (k + 1.0)) / (n - k - 1.0)
    return aic + correction
