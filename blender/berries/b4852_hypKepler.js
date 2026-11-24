// hypKepler
//
// Copied verbatim from https://github.com/bitterstoat/orrery
//   file js/orrery/src/spacetime.js, line 50
//   licence (as GitHub reports it): CC0-1.0   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function hypKepler(e, m) { // numerical approximation of hyperbolic Kepler's equation
    let result = 0;
    let lastResult, delta;
    const tolerance = 0.00000001;
    do {
        lastResult = result;
        result = e * Math.sinh(m) - m;
        delta = result - lastResult;
    }
    while ( Math.abs(delta) > tolerance );
    return result;
}
