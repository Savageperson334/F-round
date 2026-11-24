// capRing
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/tuner/scripts/simplify-landcover-globe.mjs, line 249
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function closeRing(ring) {
  if (!ring.length) return ring;
  const a = ring[0];
  const b = ring[ring.length - 1];
  if (a[0] !== b[0] || a[1] !== b[1]) ring.push([a[0], a[1]]);
  return ring;
}


function dist2(a, b) {
  const dx = a[0] - b[0];
  const dy = a[1] - b[1];
  return dx * dx + dy * dy;
}


function hypot(dx, dy) {
  return Math.sqrt(dx * dx + dy * dy);
}


function perpDist(p, a, b) {
  const dx = b[0] - a[0];
  const dy = b[1] - a[1];
  const len2 = dx * dx + dy * dy;
  if (len2 < 1e-18) return Math.sqrt(dist2(p, a));
  const t = Math.max(0, Math.min(1, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / len2));
  return hypot(p[0] - (a[0] + t * dx), p[1] - (a[1] + t * dy));
}


function rdp(points, eps) {
  if (!points || points.length <= 4) return points;
  const last = points.length - 1;
  let maxD = -1;
  let idx = 0;
  for (let i = 1; i < last; i++) {
    const d = perpDist(points[i], points[0], points[last]);
    if (d > maxD) {
      maxD = d;
      idx = i;
    }
  }
  if (maxD > eps) {
    const left = rdp(points.slice(0, idx + 1), eps);
    const right = rdp(points.slice(idx), eps);
    return left.slice(0, -1).concat(right);
  }
  return [points[0], points[last]];
}


function capRing(body, eps, maxVerts) {
  let simple = closeRing(rdp(body, eps));
  let cur = eps;
  while (simple.length - 1 > maxVerts && cur < 0.4) {
    cur *= 1.25;
    simple = closeRing(rdp(body, cur));
  }
  return simple;
}
