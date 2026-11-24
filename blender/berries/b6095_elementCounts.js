// elementCounts
//
// Copied verbatim from https://github.com/tintin0617/mof-visualization-skill
//   file skill/mof-visualization/scripts/cif-core.mjs, line 102
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function elementCounts(atoms) {
  const result = {};
  for (const atom of atoms) result[atom.element] = (result[atom.element] || 0) + 1;
  return result;
}
