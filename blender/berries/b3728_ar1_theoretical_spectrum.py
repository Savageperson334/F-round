# ar1_theoretical_spectrum
#
# Copied verbatim from https://github.com/syxscott/PaleoAST
#   file stratigraphy/spectral_analysis.py, line 118
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Fossil measurements and paleontology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def ar1_theoretical_spectrum(
    frequencies: np.ndarray,
    phi: float,
    dt: float,
) -> np.ndarray:
    """The normalised AR(1) red-noise power spectrum (Mann & Lees 1996, Eq. 3).

        S_AR1(f) = (1 - phi^2) / (1 - 2 phi cos(2*pi*f*dt) + phi^2)

    This is the null curve that a Lomb-Scargle periodogram is tested
    against, and it is the first term of the REDFIT rotation

        S_REDFIT(f) = (S_data(f) - S_AR1(f)) / sqrt(S_AR1(f))

    (Muellersohn et al. 1999; Watters & Solomon 2004), so anything that
    implements REDFIT needs this curve as a first-class value rather than
    a formula to re-derive. It used to be computed here and thrown away.

    Parameters
    ----------
    frequencies:
        Frequencies in cycles per unit time, as passed to the periodogram.
    phi:
        Lag-1 autocorrelation of the series, clipped to (-1, 1).
    dt:
        Mean sample spacing.

    Returns
    -------
    ndarray
        Power at each frequency, ``inf`` where the denominator is
        non-positive (which only happens as |phi| -> 1).
    """
    omega = 2.0 * np.pi * np.asarray(frequencies, dtype=float)
    denom = 1.0 - 2.0 * phi * np.cos(omega * dt) + phi**2
    return np.where(denom > 0, (1.0 - phi**2) / denom, np.inf)
