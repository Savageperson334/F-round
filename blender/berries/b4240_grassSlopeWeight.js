// grassSlopeWeight
//
// Copied verbatim from https://github.com/IceCreamYou/THREE.Terrain
//   file src/grass.js, line 180
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Procedural and generated worlds
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function grassSlopeWeight(slope, levels) {
    levels = levels || [0.47123889803846897, 0.7853981633974483];
    if (typeof slope !== 'number' || !isFinite(slope)) return 1;
    var fadeStart = Math.min(levels[0], levels[1]),
        fadeEnd = Math.max(levels[0], levels[1]);
    if (slope <= fadeStart) return 1;
    if (slope >= fadeEnd) return 0;
    var t = (slope - fadeStart) / Math.max(0.0001, fadeEnd - fadeStart),
        smooth = t * t * (3 - 2 * t);
    return 1 - smooth;
}
