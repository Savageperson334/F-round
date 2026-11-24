// fromF32
//
// Copied verbatim from https://github.com/synetica/enlink-decoder
//   file chirpstack/enLink - Chirpstack codec.js, line 384
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Sensors and telemetry
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function fromF32(byte0, byte1, byte2, byte3) {
    let bits = (byte0 << 24) | (byte1 << 16) | (byte2 << 8) | (byte3);
    let sign = ((bits >>> 31) === 0) ? 1.0 : -1.0;
    let e = ((bits >>> 23) & 0xff);
    let m = (e === 0) ? (bits & 0x7fffff) << 1 : (bits & 0x7fffff) | 0x800000;
    let f = sign * m * Math.pow(2, e - 150);
    return f;
}
