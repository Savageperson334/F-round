# similar_subtriangle_limits
#
# Copied verbatim from https://github.com/Augtumn/IsoLeadToolkit
#   file visualization/plotting/ternary.py, line 167
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

_FULL_TERNARY_LIMITS = (0.0, 1.0, 0.0, 1.0, 0.0, 1.0)

_TERNARY_APEX_XY = (0.0, 1.0)

_TERNARY_SQRT3 = 3.0 ** 0.5

_TERNARY_LEFT_XY = (-1.0 / _TERNARY_SQRT3, 0.0)

_TERNARY_LIMIT_EPSILON = 1e-9

_TERNARY_RIGHT_XY = (1.0 / _TERNARY_SQRT3, 0.0)


def _ray_exit_scale(anchor_x: float, anchor_y: float, dir_x: float, dir_y: float) -> float:
    """How far (in units of the direction vector) the ray stays inside the triangle."""
    candidates: list[float] = []
    if dir_y < 0.0:
        candidates.append(-anchor_y / dir_y)                     # y >= 0
    if dir_y > 0.0:
        candidates.append((1.0 - anchor_y) / dir_y)              # y <= 1
    upper = _TERNARY_SQRT3 * dir_x + dir_y
    if upper > 0.0:
        candidates.append(
            (1.0 - (_TERNARY_SQRT3 * anchor_x + anchor_y)) / upper  # sqrt3 x + y <= 1
        )
    lower = -_TERNARY_SQRT3 * dir_x + dir_y
    if lower > 0.0:
        candidates.append(
            (1.0 - (-_TERNARY_SQRT3 * anchor_x + anchor_y)) / lower  # -sqrt3 x + y <= 1
        )
    positive = [value for value in candidates if value > 0.0]
    if not positive:
        return float("inf")
    return min(positive)


def cartesian_to_ternary(x: float, y: float) -> tuple[float, float, float]:
    """Convert mpltern Cartesian data coordinates to (top, left, right) components."""
    t = float(y)
    r = ((1.0 - t) + _TERNARY_SQRT3 * float(x)) / 2.0
    l = (1.0 - t) - r
    return t, l, r


def similar_subtriangle_limits(
    anchor_x: float, anchor_y: float, drag_x: float, drag_y: float
) -> tuple[float, float, float, float, float, float]:
    """Ternary limits for the sub-triangle similar to the full one.

    The press point is the homothety centre; the release point ends up on the
    boundary of the resulting triangle. Dragging beyond the triangle (or not at
    all) returns the full-view limits, which callers treat as a zoom reset.
    """
    dir_x = float(drag_x) - float(anchor_x)
    dir_y = float(drag_y) - float(anchor_y)
    if abs(dir_x) < _TERNARY_LIMIT_EPSILON and abs(dir_y) < _TERNARY_LIMIT_EPSILON:
        return _FULL_TERNARY_LIMITS

    exit_scale = _ray_exit_scale(float(anchor_x), float(anchor_y), dir_x, dir_y)
    if not (exit_scale > 1.0):
        # The drag leaves the parent triangle: nothing to zoom into.
        return _FULL_TERNARY_LIMITS

    ratio = 1.0 / exit_scale
    corners = (_TERNARY_APEX_XY, _TERNARY_LEFT_XY, _TERNARY_RIGHT_XY)
    components = [
        cartesian_to_ternary(
            float(anchor_x) + ratio * (corner[0] - float(anchor_x)),
            float(anchor_y) + ratio * (corner[1] - float(anchor_y)),
        )
        for corner in corners
    ]
    limits: list[float] = []
    for values in zip(*components):
        low = max(0.0, min(1.0, min(values)))
        high = max(0.0, min(1.0, max(values)))
        if high - low < _TERNARY_LIMIT_EPSILON:
            high = min(1.0, low + _TERNARY_LIMIT_EPSILON)
            low = max(0.0, high - _TERNARY_LIMIT_EPSILON)
        limits.extend((low, high))
    return tuple(limits)
