// roundRing
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/tuner/scripts/build-region-isolate.mjs, line 155
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function roundRing(ring, digits) {
  const f = Math.pow(10, digits);
  return ring.map(function (p) {
    return [Math.round(p[0] * f) / f, Math.round(p[1] * f) / f];
  });
}
