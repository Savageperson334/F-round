// keyFromCode
//
// Copied verbatim from https://github.com/NaitLee/Cat-Printer
//   file www/accessibility.js, line 47
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Thermal printers and obsolete output
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function keyFromCode(code) {
    const map = {
        9: 'Tab'
    };
    return map[code] || String.fromCharCode(code);
}
