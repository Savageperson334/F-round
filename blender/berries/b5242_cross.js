// cross
//
// Copied verbatim from https://github.com/koansys/isat
//   file js/isat.js, line 1156
//   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
//   catalogue shelf: Satellites and orbital systems
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function cross(v1, v2) {
    'use strict';
    // Return 3d cross product vector from two 3d vectors.
    // http://knol.google.com/k/dot-product-cross-product-in-3d
    // http://rosettacode.org/wiki/Vector_products
    // Our vectors are represented as lists, for historical compatibility.
    var x1 = v1[0],
        y1 = v1[1],
        z1 = v1[2],
        x2 = v2[0],
        y2 = v2[1],
        z2 = v2[2];
    return [y1 * z2 - y2 * z1, z1 * x2 - z2 * x1, x1 * y2 - x2 * y1];
}
