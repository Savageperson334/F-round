# flatten_cubic_bezier
#
# Copied verbatim from https://github.com/Hansolox80/a1-mini-pen-plotter
#   file app/core/geometry.py, line 16
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Plotters & drawing machines
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math
import numpy as np


def flatten_cubic_bezier(
    p0: tuple[float, float],
    p1: tuple[float, float],
    p2: tuple[float, float],
    p3: tuple[float, float],
    tolerance_mm: float = 0.08,
) -> list[tuple[float, float]]:
    """Adaptively flattens a cubic Bézier curve into a polyline within `tolerance_mm` using vectorized NumPy evaluation."""
    tol = max(0.002, float(tolerance_mm)) if math.isfinite(tolerance_mm) else 0.08

    # Defensively sanitize input control points against non-finite or astronomical coordinates
    safe_pts = []
    for p in (p0, p1, p2, p3):
        try:
            x, y = float(p[0]), float(p[1])
            if not math.isfinite(x) or abs(x) > 1e12:
                x = 0.0
            if not math.isfinite(y) or abs(y) > 1e12:
                y = 0.0
            safe_pts.append((x, y))
        except (ValueError, TypeError, IndexError):
            safe_pts.append((0.0, 0.0))

    sp0, sp1, sp2, sp3 = safe_pts
    pt0 = np.array(sp0, dtype=np.float64)
    pt1 = np.array(sp1, dtype=np.float64)
    pt2 = np.array(sp2, dtype=np.float64)
    pt3 = np.array(sp3, dtype=np.float64)

    try:
        d1 = float(np.linalg.norm(pt0 - 2.0 * pt1 + pt2))
        d2 = float(np.linalg.norm(pt1 - 2.0 * pt2 + pt3))
        max_d = max(d1, d2)
    except Exception:
        max_d = 0.0

    # If practically straight collinear line segment or degenerate zero-length, return endpoints immediately
    if not math.isfinite(max_d) or max_d < 1e-7:
        return [sp0, sp3]

    # Wang's formula for Bézier subdivision steps within tolerance (protected against float overflow)
    try:
        val = np.sqrt((3.0 * max_d) / (4.0 * tol))
        if not math.isfinite(val) or val > 64:
            steps = 64
        else:
            steps = int(np.ceil(val))
    except (OverflowError, ValueError):
        steps = 64
    steps = max(2, min(steps, 64))

    t = np.linspace(0.0, 1.0, steps + 1, dtype=np.float64)[:, np.newaxis]
    t_inv = 1.0 - t

    # Vectorized cubic Bernstein polynomials: B(t) = (1-t)^3*P0 + 3(1-t)^2*t*P1 + 3(1-t)*t^2*P2 + t^3*P3
    b0 = t_inv ** 3
    b1 = 3.0 * (t_inv ** 2) * t
    b2 = 3.0 * t_inv * (t ** 2)
    b3 = t ** 3

    curve_pts = b0 * pt0 + b1 * pt1 + b2 * pt2 + b3 * pt3
    result: list[tuple[float, float]] = []
    for x, y in curve_pts:
        fx, fy = float(x), float(y)
        if math.isfinite(fx) and math.isfinite(fy):
            result.append((fx, fy))
    return result if result else [sp0, sp3]
