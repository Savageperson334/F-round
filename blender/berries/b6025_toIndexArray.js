// toIndexArray
//
// Copied verbatim from https://github.com/superstar54/weas
//   file src/utils.js, line 21
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function toIndexArray(indices, name = "indices") {
  if (indices === null) {
    throw new Error(`${name} must not be null`);
  }
  return Array.isArray(indices) ? indices : [indices];
}
