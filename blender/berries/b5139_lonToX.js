// lonToX
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/tuner/scripts/bake-night-lights.mjs, line 33
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const ZOOM = 6;

const WORLD = 256 * 2 ** ZOOM;


const lonToX = (lon) => ((lon + 180) / 360) * WORLD;
