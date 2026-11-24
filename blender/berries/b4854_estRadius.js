// estRadius
//
// Copied verbatim from https://github.com/bitterstoat/orrery
//   file js/orrery/src/spacetime.js, line 213
//   licence (as GitHub reports it): CC0-1.0   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function estRadius(h, p = 0.15) { 
    return 664.5 / Math.sqrt(p) * Math.pow( 10, h * -0.2);
}
