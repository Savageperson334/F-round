// decToMinSec
//
// Copied verbatim from https://github.com/bitterstoat/orrery
//   file js/orrery/src/spacetime.js, line 190
//   licence (as GitHub reports it): CC0-1.0   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function decToMinSec(n) { 
    const sign = Math.sign(n);
    n = Math.abs(n);
    let deg = Math.floor(n);
    let min = parseFloat(("0" + Math.floor((n - deg) * 60)).slice(-2));
    const sec = (n - deg - min/60) * 3600;
    if (sec >= 60) {
        min++;
        sec-=60;
    }
    if (min >= 60) {
        deg++;
        min-=60;
    }
    return { sign:(sign<0) ? "-" : "", deg:deg, min:min, sec:sec }
}
