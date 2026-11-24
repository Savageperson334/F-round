// hashcode
//
// Copied verbatim from https://github.com/wwwtyro/space-2d
//   file random.js, line 9
//   licence (as GitHub reports it): Unlicense   see ../licenses/
//   catalogue shelf: Procedural and generated worlds
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function hashcode(str) {
    var hash = 0;
    for (var i = 0; i < str.length; i++) {
        var char = str.charCodeAt(i)
        hash += (i + 1) * char;
    }
    return hash;
}
