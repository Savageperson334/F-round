// invertMatrix2
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/math/matrix2.js, line 79
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const determinant2 = (m) => m[0] * m[3] - m[1] * m[2];


const invertMatrix2 = (m) => {
	const det = determinant2(m);
	if (
		Math.abs(det) < 1e-12 ||
		Number.isNaN(det) ||
		!Number.isFinite(m[4]) ||
		!Number.isFinite(m[5])
	) {
		return undefined;
	}
	return [
		m[3] / det,
		-m[1] / det,
		-m[2] / det,
		m[0] / det,
		(m[2] * m[5] - m[3] * m[4]) / det,
		(m[1] * m[4] - m[0] * m[5]) / det,
	];
};
