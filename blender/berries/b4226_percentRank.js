// percentRank
//
// Copied verbatim from https://github.com/IceCreamYou/THREE.Terrain
//   file src/analysis.js, line 383
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Procedural and generated worlds
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function percentRank(arr, v) {
    if (typeof v !== 'number') throw new TypeError('v must be a number');
    for (var i = 0, l = arr.length; i < l; i++) {
        if (v <= arr[i]) {
            while (i < l && v === arr[i]) {
                i++;
            }
            if (i === 0) return 0;
            if (v !== arr[i-1]) {
                i += (v - arr[i-1]) / (arr[i] - arr[i-1]);
            }
            return i / l;
        }
    }
    return 1;
}
