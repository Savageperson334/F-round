// wrapIndex
//
// Copied verbatim from https://github.com/superstar54/weas
//   file src/geometry/marchingCubes.js, line 303
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function wrapIndex(value, size) {
  const m = value % size;
  return m < 0 ? m + size : m;
}
