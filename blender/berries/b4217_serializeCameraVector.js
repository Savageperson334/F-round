// serializeCameraVector
//
// Copied verbatim from https://github.com/IceCreamYou/THREE.Terrain
//   file demo/main.js, line 25
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Procedural and generated worlds
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function serializeCameraVector(values) {
    return values.map(function(value) { return Number(value.toFixed(6)); }).join(',');
}
