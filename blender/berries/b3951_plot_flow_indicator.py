# plot_flow_indicator
#
# Copied verbatim from https://github.com/xandergos/terrain-diffusion
#   file terrain_diffusion/inference/postprocessing.py, line 68
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def d8_flow(z, tol=1e-3):
    z = np.asarray(z)
    H, W = z.shape
    dy = np.array([-1,  1,  0,  0, -1, -1,  1,  1], dtype=int)
    dx = np.array([ 0,  0, -1,  1, -1,  1, -1,  1], dtype=int)
    dist = np.array([1, 1, 1, 1, np.sqrt(2), np.sqrt(2), np.sqrt(2), np.sqrt(2)], dtype=z.dtype)

    zpad = np.pad(z, 1, mode='edge')
    nbrs = np.stack([zpad[1+dy[k]:1+dy[k]+H, 1+dx[k]:1+dx[k]+W] for k in range(8)], axis=0)
    slopes = (z[None] - nbrs) / dist[:, None, None]  # positive = downhill
    slopes[slopes < tol] = -np.inf

    # Ocean handling
    # - Centers that are NaN or <= 0 are sinks (ocean)
    # - Neighbors that are NaN or <= 0 act as ocean sinks: prefer routing into them
    center_ocean = np.isnan(z) | (z <= 0)
    neighbor_ocean = np.isnan(nbrs) | (nbrs <= 0)

    # Prepare two slope tensors:
    # 1) prefer_nan: prefers routing into NaN neighbors (treat as +inf slope)
    # 2) ignore_nan: ignores NaN neighbors (treat as -inf) to decide internal sinks
    prefer_ocean = slopes.copy()
    prefer_ocean[:, center_ocean] = -np.inf
    prefer_ocean[neighbor_ocean & (~center_ocean[None])] = np.inf

    ignore_ocean = slopes.copy()
    ignore_ocean[:, center_ocean] = -np.inf
    ignore_ocean[neighbor_ocean] = -np.inf

    # Chosen directions prefer draining into NaN neighbors (coast/ocean)
    kmax = np.argmax(prefer_ocean, axis=0)
    max_slope_prefer = np.take_along_axis(prefer_ocean, kmax[None], axis=0)[0]

    # is_sink: true only if center is NaN OR there is no downhill route ignoring NaNs
    max_slope_ignore = np.take_along_axis(ignore_ocean, np.argmax(ignore_ocean, axis=0)[None], axis=0)[0]
    has_ocean_neighbor = np.any(neighbor_ocean, axis=0)
    is_sink = center_ocean | ((~has_ocean_neighbor) & (~np.isfinite(max_slope_ignore)))

    rr = np.clip(np.arange(H)[:, None] + dy[kmax], 0, H - 1)
    cc = np.clip(np.arange(W)[None, :] + dx[kmax], 0, W - 1)
    return rr, cc, is_sink, kmax


def flow_accumulation(z, rr, cc, is_sink):
    H, W = z.shape
    invalid = np.isnan(z) | (z <= 0)
    # Initialize with ones for valid cells only
    A = np.zeros((H, W), dtype=np.float32)
    A[~invalid] = 1.0

    # Process cells from high to low elevation, ignoring NaNs
    flat_idx = np.flatnonzero(~invalid)
    if flat_idx.size:
        vals = z.ravel()[flat_idx]
        order = flat_idx[np.argsort(vals)[::-1]]
        r, c = order // W, order % W
        for i, j in zip(r, c):
            if not is_sink[i, j]:
                ti, tj = rr[i, j], cc[i, j]
                if not invalid[ti, tj]:
                    A[ti, tj] += A[i, j]
    return A


def plot_flow_indicator(z, max_pool_kernel=1):
    z = np.asarray(z)
    rr, cc, is_sink, kmax = d8_flow(z)
    A = flow_accumulation(z, rr, cc, is_sink)
    # Ensure ocean (NaN or <= 0) remain non-contributing in the indicator
    invalid = np.isnan(z) | (z <= 0)
    A[invalid] = 0.0

    # Perform max pooling on A, configurable by max_pool_kernel
    if max_pool_kernel > 1:
        # Downsampling max pool (non-overlapping, stride = kernel size)
        new_H = A.shape[0] // max_pool_kernel
        new_W = A.shape[1] // max_pool_kernel
        A = A[:new_H * max_pool_kernel, :new_W * max_pool_kernel]
        A = A.reshape(new_H, max_pool_kernel, new_W, max_pool_kernel)
        A = A.max(axis=(1, 3))

    return np.log1p(A)
