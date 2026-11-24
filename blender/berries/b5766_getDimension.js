// getDimension
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/math/polygon.js, line 166
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const getDimension = (points) => {
	for (let i = 0; i < points.length; i += 1) {
		if (points[i] && points[i].length) {
			return points[i].length;
		}
	}
	return 0;
};
