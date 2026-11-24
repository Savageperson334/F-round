# cosine_scheduler_step
#
# Copied verbatim from https://github.com/earthspecies/avex
#   file avex/models/atst_frame/atst_frame.py, line 1435
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def cosine_scheduler_step(
    base_value: float,
    final_value: float,
    max_steps: int,
    warmup_steps: int = 0,
    start_warmup_value: float = 0,
) -> np.ndarray:
    """Create cosine learning rate schedule.

    Args:
        base_value: Base learning rate value
        final_value: Final learning rate value
        max_steps: Maximum number of steps
        warmup_steps: Number of warmup steps
        start_warmup_value: Starting warmup value

    Returns:
        np.ndarray: Learning rate schedule
    """
    warmup_schedule = np.array([])
    if warmup_steps > 0:
        warmup_schedule = np.linspace(start_warmup_value, base_value, warmup_steps)

    iters = np.arange(max_steps - warmup_steps)
    schedule = final_value + 0.5 * (base_value - final_value) * (1 + np.cos(np.pi * iters / len(iters)))

    schedule = np.concatenate((warmup_schedule, schedule))
    assert len(schedule) == max_steps
    return schedule
