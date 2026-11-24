// maxArraysLength
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/graph/count.js, line 17
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const maxArraysLength = (arrays) =>
	Math.max(0, ...arrays.filter((el) => el !== undefined).map((el) => el.length));
