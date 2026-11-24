// keyToLetter
//
// Copied verbatim from https://github.com/NaitLee/Cat-Printer
//   file www/accessibility.js, line 38
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Thermal printers and obsolete output
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function keyToLetter(key) {
    const map = {
        ' ': 'SPACE',
        ',': 'COMMA',
        '.': "DOT"
    };
    return map[key] || key;
}
