# kind_for_status
#
# Copied verbatim from https://github.com/chrisfulcher/orrery
#   file src/orrery/sam/client.py, line 48
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def kind_for_status(status_code: int) -> str:
    """Name a failure from the status the server gave. 404 is permanent and 429 or a 5xx is
    worth another try tomorrow, which is the distinction a retry policy needs and the one a
    bare 'failed' throws away."""
    if status_code == 404:
        return "gone"
    if status_code == 429:
        return "rate_limited"
    if status_code >= 500:
        return "server_error"
    if status_code >= 400:
        return "client_error"
    return "failed"
