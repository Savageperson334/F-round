// bboxOf
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/tuner/scripts/patch-china-boundaries.mjs, line 161
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function bboxOf(coords) {
  let minLng = 180;
  let maxLng = -180;
  let minLat = 90;
  let maxLat = -90;
  const walk = (node) => {
    if (typeof node[0] === 'number') {
      minLng = Math.min(minLng, node[0]);
      maxLng = Math.max(maxLng, node[0]);
      minLat = Math.min(minLat, node[1]);
      maxLat = Math.max(maxLat, node[1]);
    } else node.forEach(walk);
  };
  walk(coords);
  return [minLng, minLat, maxLng, maxLat];
}
