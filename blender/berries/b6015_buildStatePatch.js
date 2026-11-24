// buildStatePatch
//
// Copied verbatim from https://github.com/superstar54/weas
//   file src/operation/baseOperation.js, line 262
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function buildStatePatch(path, patch) {
  if (!path) {
    return patch;
  }
  const parts = path.split(".");
  const root = {};
  let current = root;
  for (let i = 0; i < parts.length - 1; i++) {
    current[parts[i]] = {};
    current = current[parts[i]];
  }
  current[parts[parts.length - 1]] = patch;
  return root;
}
