// snap
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/tuner/scripts/simplify-landcover-globe.mjs, line 108
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const GRID = 0.04;


function snap(p) {
  return [
    Math.round(p[0] / GRID) * GRID,
    Math.round(p[1] / GRID) * GRID,
  ];
}
