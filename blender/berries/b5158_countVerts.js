// countVerts
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/tuner/scripts/build-region-isolate.mjs, line 169
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function countVerts(polys) {
  let n = 0;
  for (const poly of polys) {
    for (const ring of poly) n += ring.length;
  }
  return n;
}
