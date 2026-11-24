// toFixed
//
// Copied verbatim from https://github.com/vsr83/Bessel3d
//   file app.js, line 46
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical observation tools
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


let toFixed = function(num) {
    if (num < 10)
        return "0" + num;
    else 
        return num;
}
