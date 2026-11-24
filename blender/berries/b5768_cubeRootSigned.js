// cubeRootSigned
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/math/polynomial.js, line 11
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const cubeRootSigned = (n) => (n < 0 ? -((-n) ** (1 / 3)) : n ** (1 / 3));
