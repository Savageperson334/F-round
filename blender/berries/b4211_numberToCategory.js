// numberToCategory
//
// Copied verbatim from https://github.com/IceCreamYou/THREE.Terrain
//   file demo/analytics.js, line 89
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Procedural and generated worlds
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function numberToCategory(value, buckets) {
    buckets = buckets || [-2, -2 / 3, 2 / 3, 2];
    if (typeof buckets.length === 'number' && buckets.length > 3) {
        if (value < buckets[0]) return 'very low';
        if (value < buckets[1]) return 'low';
        if (value < buckets[2]) return 'medium';
        if (value < buckets[3]) return 'high';
        return 'very high';
    }
    var keys = Object.keys(buckets).sort(function(first, second) {
        return buckets[first] - buckets[second];
    });
    for (var index = 0; index < keys.length; index++) {
        if (value < buckets[keys[index]]) return keys[index];
    }
    return keys[keys.length - 1];
}
