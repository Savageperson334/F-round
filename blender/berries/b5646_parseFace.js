// parseFace
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/convert/objToFold.js, line 75
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const parseFace = (face) => face.slice(1).map((str) => parseInt(str, 10) - 1);
