// intersectionOfStrings
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/graph/validate/validateReferences.js, line 14
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const intersectionOfStrings = (array1, array2) => {
	const counts = {};
	array1.forEach((key) => {
		counts[key] = 1;
	});
	array2.forEach((key) => {
		counts[key] = counts[key] === 1 ? 2 : 1;
	});
	return Object.keys(counts).filter((key) => counts[key] === 2);
};
