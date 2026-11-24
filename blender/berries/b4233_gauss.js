// gauss
//
// Copied verbatim from https://github.com/IceCreamYou/THREE.Terrain
//   file src/gaussian.js, line 78
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Procedural and generated worlds
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function gauss(x, s) {
    // 2.5066282746310005 is sqrt(2*pi)
    return Math.exp(-0.5 * x*x / (s*s)) / (s * 2.5066282746310005);
}
