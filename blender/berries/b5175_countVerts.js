// countVerts
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/tuner/scripts/patch-china-boundaries.mjs, line 150
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function countVerts(coords) {
  let n = 0;
  const walk = (node) => {
    if (!node) return;
    if (typeof node[0] === 'number') n += 1;
    else node.forEach(walk);
  };
  walk(coords);
  return n;
}
