// fade
//
// Copied verbatim from https://github.com/IceCreamYou/THREE.Terrain
//   file src/noise.js, line 151
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Procedural and generated worlds
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function fade(t) {
    return t*t*t*(t*(t*6-15)+10);
}
