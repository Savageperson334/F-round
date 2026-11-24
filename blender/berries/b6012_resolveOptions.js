// resolveOptions
//
// Copied verbatim from https://github.com/superstar54/weas
//   file src/operation/baseOperation.js, line 201
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function resolveOptions(options, op) {
  if (!options) {
    return null;
  }
  if (typeof options === "function") {
    return options(op);
  }
  return options;
}
