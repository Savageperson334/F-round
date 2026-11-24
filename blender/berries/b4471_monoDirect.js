// monoDirect
//
// Copied verbatim from https://github.com/NaitLee/Cat-Printer
//   file www/image.js, line 35
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Thermal printers and obsolete output
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function monoDirect(mono, _w, _h) {
    for(let i = 0; i < mono.length; ++i){
        mono[i] = mono[i] > 0x80 ? 0xff : 0x00;
    }
    return mono;
}
