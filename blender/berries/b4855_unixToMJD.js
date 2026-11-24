// unixToMJD
//
// Copied verbatim from https://github.com/bitterstoat/orrery
//   file js/orrery/src/spacetime.js, line 258
//   licence (as GitHub reports it): CC0-1.0   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const DayInMillis = 86400000;

const UnixTimeZeroInMJD = 40587;


function unixToMJD(d) { 
    return d / DayInMillis + UnixTimeZeroInMJD; 
}
