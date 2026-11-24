// roundPt
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/tuner/scripts/patch-china-boundaries.mjs, line 122
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function roundPt(p) {
  return [Math.round(p[0] * 1e4) / 1e4, Math.round(p[1] * 1e4) / 1e4];
}
