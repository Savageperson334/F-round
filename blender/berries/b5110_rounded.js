// rounded
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/runtime/benchmark-vector-tuning.mjs, line 411
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function rounded(value, digits) {
  if (!Number.isFinite(value)) return null;
  return Number(value.toFixed(digits == null ? 2 : digits));
}
