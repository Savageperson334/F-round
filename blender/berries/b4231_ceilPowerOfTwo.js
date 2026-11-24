// ceilPowerOfTwo
//
// Copied verbatim from https://github.com/IceCreamYou/THREE.Terrain
//   file src/core.js, line 12
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Procedural and generated worlds
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function ceilPowerOfTwo(n) {
    return Math.pow(2, Math.ceil(Math.log(n) / Math.log(2)));
}
