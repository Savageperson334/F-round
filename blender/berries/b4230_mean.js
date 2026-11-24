// mean
//
// Copied verbatim from https://github.com/IceCreamYou/THREE.Terrain
//   file src/analysis.js, line 841
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Procedural and generated worlds
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function mean(data) {
    var sum = 0,
        l = data.length;
    for (var i = 0; i < l; i++) {
        sum += data[i];
    }
    return sum / l;
}
