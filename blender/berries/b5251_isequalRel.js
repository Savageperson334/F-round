// isequalRel
//
// Copied verbatim from https://github.com/koansys/isat
//   file js/test_utils.js, line 4
//   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
//   catalogue shelf: Satellites and orbital systems
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function isequalRel(x, y, tol) {
    var EPS = Math.pow(2, -52); // IEEE 754 double precision epsilon
    if (Math.abs(x - y) <= (tol * Math.max(Math.abs(x), Math.abs(y)) + EPS)) {
        return true;
    }
    // Too bad this stops QUnit test, but is handy for finding want/got values
    //throw Error("isEqualRel x=" + x + " y=" + y + "  tol=" + tol);
    return false;
}
