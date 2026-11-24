# circulation
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file book_chapters/particles.py, line 181
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np

KEY = 1 << 32


def _pressure(iu: np.ndarray, iv: np.ndarray, flow: np.ndarray, n: int, tol: float = 1e-6,
              iters: int = 5000) -> np.ndarray:
    """
    The potential phi whose differences phi(u) − phi(v) explain as much of the
    flow as possible: least squares, by conjugate gradients on the network's
    Laplacian, preconditioned by the degrees (research/oee/checks/circulation.py).
    """
    deg = (np.bincount(iu, minlength=n) + np.bincount(iv, minlength=n)).astype(float)

    def lap(x: np.ndarray) -> np.ndarray:
        return deg * x - np.bincount(iu, weights=x[iv], minlength=n) - np.bincount(iv, weights=x[iu], minlength=n)

    d = np.bincount(iu, weights=flow, minlength=n) - np.bincount(iv, weights=flow, minlength=n)
    inv = 1.0 / np.maximum(deg, 1.0)
    x = np.zeros(n)
    r = d.copy()
    z = inv * r
    p = z.copy()
    rz = r @ z
    dd = max(d @ d, 1e-300)
    for _ in range(iters):
        if r @ r <= tol * tol * dd:
            break
        ap = lap(p)
        alpha = rz / (p @ ap)
        x += alpha * p
        r -= alpha * ap
        z = inv * r
        rz_new = r @ z
        p = z + (rz_new / rz) * p
        rz = rz_new
    return x


def circulation(keys: np.ndarray, flow: np.ndarray) -> np.ndarray:
    """
    The part of a net flow (one value a connection, keyed lower·KEY + higher)
    that goes round loops. A connection on no loop — on a dead-end branch —
    carries none of it, and the rest does not depend on such connections, so
    they are pruned first, dead end by dead end, down to the network's core:
    the same answer, and far fewer, far better behaved equations to solve.
    """
    u, v = keys // KEY, keys % KEY
    _, inverse = np.unique(np.concatenate([u, v]), return_inverse=True)
    iu, iv = inverse[:len(u)], inverse[len(u):]
    n = int(inverse.max()) + 1
    keep = np.ones(len(keys), dtype=bool)
    while True:
        deg = np.bincount(iu[keep], minlength=n) + np.bincount(iv[keep], minlength=n)
        dead = keep & ((deg[iu] == 1) | (deg[iv] == 1))
        if not dead.any():
            break
        keep &= ~dead
    out = np.zeros(len(keys))
    if keep.any():
        cu, cv, cf = iu[keep], iv[keep], flow[keep]
        _, back = np.unique(np.concatenate([cu, cv]), return_inverse=True)
        bu, bv = back[:len(cu)], back[len(cu):]
        phi = _pressure(bu, bv, cf, int(back.max()) + 1)
        out[keep] = cf - (phi[bu] - phi[bv])
    return out
