// roundNumber
//
// Copied verbatim from https://github.com/IceCreamYou/THREE.Terrain
//   file demo/analytics.js, line 48
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Procedural and generated worlds
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function roundNumber(value, places) {
    places = places || 0;
    var multiplier = Math.pow(10, places | 0);
    return Math.round(value * multiplier) / multiplier;
}
