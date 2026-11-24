// cloneValue
//
// Copied verbatim from https://github.com/superstar54/weas
//   file src/state/store.js, line 1
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function cloneValue(value) {
  const json = JSON.stringify(value);
  if (json === undefined) {
    return undefined;
  }
  return JSON.parse(json);
}
