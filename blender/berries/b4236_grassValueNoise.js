// grassValueNoise
//
// Copied verbatim from https://github.com/IceCreamYou/THREE.Terrain
//   file src/grass.js, line 80
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Procedural and generated worlds
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function grassNoiseHash(x, y) {
    var value = Math.sin(x * 127.1 + y * 311.7) * 43758.5453;
    return value - Math.floor(value);
}


function grassValueNoise(x, y) {
    var x0 = Math.floor(x),
        y0 = Math.floor(y),
        tx = x - x0,
        ty = y - y0,
        sx = tx * tx * (3 - 2 * tx),
        sy = ty * ty * (3 - 2 * ty),
        n00 = grassNoiseHash(x0, y0),
        n10 = grassNoiseHash(x0 + 1, y0),
        n01 = grassNoiseHash(x0, y0 + 1),
        n11 = grassNoiseHash(x0 + 1, y0 + 1),
        nx0 = n00 + (n10 - n00) * sx,
        nx1 = n01 + (n11 - n01) * sx;
    return nx0 + (nx1 - nx0) * sy;
}
