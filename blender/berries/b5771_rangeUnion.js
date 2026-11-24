// rangeUnion
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/math/range.js, line 15
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const rangeUnion = (a, b) => {
	const bSorted = b[0] <= b[1];
	return a[0] <= a[1]
		? [Math.min(a[0], bSorted ? b[0] : b[1]), Math.max(a[1], bSorted ? b[1] : b[0])]
		: [Math.min(a[1], bSorted ? b[0] : b[1]), Math.max(a[0], bSorted ? b[1] : b[0])];
};
