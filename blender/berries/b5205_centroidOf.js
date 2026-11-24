// centroidOf
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/tuner/scripts/simplify-landcover-globe.mjs, line 156
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function centroidOf(ring) {
  let x = 0;
  let y = 0;
  const body = ring.slice(0, -1);
  const n = body.length || 1;
  for (let i = 0; i < body.length; i++) {
    x += body[i][0];
    y += body[i][1];
  }
  return [x / n, y / n];
}
