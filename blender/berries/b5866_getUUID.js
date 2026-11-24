// getUUID
//
// Copied verbatim from https://github.com/rewonc/pastalog
//   file src/lib.js, line 31
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Graphs and networks
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function getUUID(modelName, seriesName) {
  return `${modelName}/${seriesName}`;
}
