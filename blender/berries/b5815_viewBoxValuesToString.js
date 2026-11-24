// viewBoxValuesToString
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/svg/arguments/makeViewBox.js, line 16
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const viewBoxValuesToString = function (x, y, width, height, padding = 0) {
	const scale = 1.0;
	const d = width / scale - width;
	const X = x - d - padding;
	const Y = y - d - padding;
	const W = width + d * 2 + padding * 2;
	const H = height + d * 2 + padding * 2;
	return [X, Y, W, H].join(" ");
};
