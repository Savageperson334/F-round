// expandFill
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/tuner/scripts/simplify-landcover-globe.mjs, line 216
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function signedArea(ring) {
  let a = 0;
  for (let i = 0, j = ring.length - 1; i < ring.length; j = i++) {
    a += ring[j][0] * ring[i][1] - ring[i][0] * ring[j][1];
  }
  return a / 2;
}


function hypot(dx, dy) {
  return Math.sqrt(dx * dx + dy * dy);
}


function closeRing(ring) {
  if (!ring.length) return ring;
  const a = ring[0];
  const b = ring[ring.length - 1];
  if (a[0] !== b[0] || a[1] !== b[1]) ring.push([a[0], a[1]]);
  return ring;
}


function expandFill(ring, pad) {
  const area = signedArea(ring);
  if (!isFinite(area) || Math.abs(area) < 1e-12) return ring;
  const body = ring.slice(0, -1);
  const n = body.length;
  if (n < 3) return ring;
  const sign = area >= 0 ? 1 : -1;
  const out = [];
  for (let i = 0; i < n; i++) {
    const a = body[(i - 1 + n) % n];
    const b = body[i];
    const c = body[(i + 1) % n];
    const e1x = b[0] - a[0];
    const e1y = b[1] - a[1];
    const e2x = c[0] - b[0];
    const e2y = c[1] - b[1];
    const l1 = hypot(e1x, e1y) || 1;
    const l2 = hypot(e2x, e2y) || 1;
    // CCW left normal points interior when area > 0. Expand fill = opposite.
    const n1x = -e1y / l1;
    const n1y = e1x / l1;
    const n2x = -e2y / l2;
    const n2y = e2x / l2;
    let nx = n1x + n2x;
    let ny = n1y + n2y;
    const ln = hypot(nx, ny) || 1;
    nx /= ln;
    ny /= ln;
    out.push([b[0] - sign * pad * nx, b[1] - sign * pad * ny]);
  }
  return closeRing(out);
}
