// formatNumber
//
// Copied verbatim from https://github.com/superstar54/weas
//   file src/io/structure.js, line 5
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function formatNumber(value) {
  if (typeof value !== "number" || Number.isNaN(value)) {
    return "0";
  }
  return value.toFixed(6);
}
