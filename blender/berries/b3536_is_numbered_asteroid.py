# is_numbered_asteroid
#
# Copied verbatim from https://github.com/rlseaman/neolyzer
#   file scripts/partition_mpcorb.py, line 61
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def is_numbered_asteroid(packed):
    """
    Check if a packed designation represents a numbered asteroid.

    MPC packed designation format:
    - Numbered asteroids: 5 characters or fewer (after stripping spaces)
      - 00001-99999: 5 digits with leading zeros
      - 100000+: Letter prefix + 4 chars (A0001, B0001, ..., ~xxxx)
    - Provisional designations: 7 characters
      - Century code (I=1800s, J=1900s, K=2000s) + year + half-month + serial

    The key distinction is length: numbered <= 5 chars, provisional = 7 chars.
    """
    if not packed:
        return False

    # After strip(), numbered asteroids are <= 5 chars, provisional are 7
    return len(packed) <= 5
