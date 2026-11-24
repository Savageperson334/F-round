// splitLongEdges
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/tuner/scripts/simplify-landcover-globe.mjs, line 197
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


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


function splitLongEdges(ring, maxLen) {
  const body = ring.slice(0, -1);
  const out = [];
  for (let i = 0; i < body.length; i++) {
    const a = body[i];
    const b = body[(i + 1) % body.length];
    out.push(a);
    const dx = b[0] - a[0];
    const dy = b[1] - a[1];
    const d = hypot(dx, dy);
    const steps = Math.max(1, Math.ceil(d / maxLen));
    for (let s = 1; s < steps; s++) {
      const t = s / steps;
      out.push([a[0] + dx * t, a[1] + dy * t]);
    }
  }
  return closeRing(out);
}
