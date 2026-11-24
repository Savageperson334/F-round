# validate_worker_count
#
# Copied verbatim from https://github.com/microsoft/haste
#   file hastelib/src/hastegeo/core/utils/parallel.py, line 22
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

_MAX_CONFIGURED_WORKERS = 64


def validate_worker_count(value: int, name: str = "max_workers") -> int:
    """Validate a worker count before constructing or scheduling a pool."""
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")
    if not 1 <= value <= _MAX_CONFIGURED_WORKERS:
        raise ValueError(
            f"{name} must be between 1 and {_MAX_CONFIGURED_WORKERS}"
        )
    return value
