// bboxOverlap
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/tuner/scripts/build-region-isolate.mjs, line 341
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function bboxOverlap(a, b) {
  return a[0] <= b[2] && a[2] >= b[0] && a[1] <= b[3] && a[3] >= b[1];
}
