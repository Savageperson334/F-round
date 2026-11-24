// latRing
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/tuner/scripts/build-polar-ice.mjs, line 63
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


function latRing(lat, steps, clockwise) {
  const ring = [];
  for (let i = 0; i <= steps; i++) {
    const t = clockwise ? (steps - i) : i;
    const lon = -180 + (360 * t) / steps;
    ring.push([lon, lat]);
  }
  return closeRing(ring);
}
