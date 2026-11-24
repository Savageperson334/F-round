// parseDemoSeed
//
// Copied verbatim from https://github.com/IceCreamYou/THREE.Terrain
//   file demo/settings.js, line 11
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Procedural and generated worlds
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function parseDemoSeed(value) {
    if (!value || !/^(?:0x[0-9a-f]+|\d+)$/i.test(value)) return null;
    var seed = Number(value);
    return Number.isSafeInteger(seed) ? seed >>> 0 : null;
}
