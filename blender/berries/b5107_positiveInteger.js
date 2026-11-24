// positiveInteger
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/runtime/benchmark-vector-tuning.mjs, line 111
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function positiveInteger(value, name, minimum) {
  const number = Number(value);
  if (!Number.isInteger(number) || number < minimum) {
    throw new Error(name + ' must be an integer >= ' + minimum + ', got ' + value);
  }
  return number;
}
