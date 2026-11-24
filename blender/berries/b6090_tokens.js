// tokens
//
// Copied verbatim from https://github.com/tintin0617/mof-visualization-skill
//   file skill/mof-visualization/scripts/cif-core.mjs, line 3
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function tokens(line) {
  return line.match(/(?:[^\s"']+|"[^"]*"|'[^']*')+/g)?.map((value) => value.replace(/^['"]|['"]$/g, '')) ?? [];
}
