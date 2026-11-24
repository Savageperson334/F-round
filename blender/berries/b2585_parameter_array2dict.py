# parameter_array2dict
#
# Copied verbatim from https://github.com/lmizrahi/etas
#   file etas/inversion.py, line 475
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def parameter_array2dict(theta):
    """Convert an array of ETAS parameters to a dict.

    Parameters
    ----------
    theta : array-like
        Parameters in the order log10_mu, log10_iota, log10_k0, a, log10_c,
        omega, log10_tau, log10_d, gamma, rho. If it has 11 entries, the first
        one is ``alpha``.

    Returns
    -------
    dict
        Parameter name -> value.
    """
    if len(theta) > 10:
        return dict(
            zip(
                [
                    "alpha",
                    "log10_mu",
                    "log10_iota",
                    "log10_k0",
                    "a",
                    "log10_c",
                    "omega",
                    "log10_tau",
                    "log10_d",
                    "gamma",
                    "rho",
                ],
                theta,
            )
        )

    return dict(
        zip(
            [
                "log10_mu",
                "log10_iota",
                "log10_k0",
                "a",
                "log10_c",
                "omega",
                "log10_tau",
                "log10_d",
                "gamma",
                "rho",
            ],
            theta,
        )
    )
