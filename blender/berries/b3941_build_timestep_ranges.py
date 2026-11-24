# build_timestep_ranges
#
# Copied verbatim from https://github.com/xandergos/terrain-diffusion
#   file annotated_infinite_panorama.py, line 84
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def build_timestep_ranges(all_timesteps, thresholds):
    """Partition descending ``all_timesteps`` into phases using ``thresholds``.
    Phase 0 gets ``t >= thresholds[0]``, the last phase gets
    ``t < thresholds[-1]``, intermediate phases fill the gaps."""
    thresholds = sorted(thresholds, reverse=True)
    if not thresholds:
        return [all_timesteps]
    ranges = []
    prev = None
    for t in thresholds:
        r = all_timesteps[all_timesteps >= t] if prev is None \
            else all_timesteps[(all_timesteps >= t) & (all_timesteps < prev)]
        if len(r) > 0:
            ranges.append(r)
        prev = t
    tail = all_timesteps[all_timesteps < thresholds[-1]]
    if len(tail) > 0:
        ranges.append(tail)
    return ranges
