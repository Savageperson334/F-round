// requireText
//
// Copied verbatim from https://github.com/tintin0617/mof-visualization-skill
//   file skill/mof-visualization/scripts/material-config.mjs, line 15
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function requireText(value, message) {
  if (typeof value !== 'string' || !value.trim()) throw new Error(message);
  return value.trim();
}
