# resolve_job_id
#
# Copied verbatim from https://github.com/microsoft/haste
#   file hastelib/src/hastegeo/core/utils/batch_config.py, line 83
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

MAX_JOB_ID_LENGTH = 64


def resolve_job_id(base_job_id, selected_pool, candidate_pool_ids=None):
    """Return the Batch job id to use for a task routed to ``selected_pool``.

    A Batch job is permanently bound to the pool it was created against, and
    can only be re-pointed while it has no active tasks. Capacity-aware routing
    picks the pool per task, so reusing one static job id across pools breaks as
    soon as two tasks are in flight on different pools. Scoping the job id to
    the selected pool gives one job per pool and removes the conflict.

    Environments that are not routing across multiple pools keep their existing
    job id, so their jobs are not renamed.

    Args:
        base_job_id: The configured job id (e.g. ``IMAGERYPREP_BATCH_JOB_ID``).
        selected_pool: The pool this task was routed to.
        candidate_pool_ids: The pools routing may choose between.
    """
    if not selected_pool:
        return base_job_id
    candidates = list(candidate_pool_ids or [])

    # The default convention is job id == pool id, so follow the selected pool
    # and keep names clean rather than doubling the pool id up.
    if base_job_id in candidates:
        return selected_pool[:MAX_JOB_ID_LENGTH]

    # A single candidate cannot spill over, so leave custom ids untouched.
    if len(candidates) <= 1:
        return base_job_id

    # Reserve room for the suffix: truncating the base instead of the pool
    # keeps ids for two different pools distinct.
    room = MAX_JOB_ID_LENGTH - len(selected_pool) - 1
    if room <= 0:
        return selected_pool[:MAX_JOB_ID_LENGTH]
    return f"{base_job_id[:room]}-{selected_pool}"
