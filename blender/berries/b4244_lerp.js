// lerp
//
// Copied verbatim from https://github.com/IceCreamYou/THREE.Terrain
//   file src/noise.js, line 155
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Procedural and generated worlds
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function lerp(a, b, t) {
    return (1-t)*a + t*b;
}
