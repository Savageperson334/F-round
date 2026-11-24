// clampLat
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/tuner/scripts/build-polar-ice.mjs, line 50
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const LAT_MAX = 85;


function clampLat(lat) {
  return Math.max(-LAT_MAX, Math.min(LAT_MAX, lat));
}
