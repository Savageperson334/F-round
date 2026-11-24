// matrixFormSkewY
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/svg/general/transforms.js, line 86
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const matrixFormSkewY = function (params) {
	return [1, Math.tan((params[0] * Math.PI) / 180), 0, 1, 0, 0];
};
