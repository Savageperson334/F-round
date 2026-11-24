// bondVisualStyle
//
// Copied verbatim from https://github.com/tintin0617/mof-visualization-skill
//   file skill/mof-visualization/scripts/render-core.mjs, line 41
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function bondVisualStyle(elementA, elementB, depth) {
  const pair = [elementA, elementB].sort().join('-');
  const coordination = ['O-Zr', 'N-Zn', 'Co-N', 'Al-O', 'Fe-O', 'Cr-O', 'Ni-O', 'O-Ti', 'Cu-O'].includes(pair);
  return coordination
    ? { color: 'rgba(79, 183, 214, ' + (0.42 + 0.52 * depth) + ')', widthMultiplier: 1.32 }
    : { color: 'rgba(132, 158, 188, ' + (0.28 + 0.58 * depth) + ')', widthMultiplier: 1 };
}
