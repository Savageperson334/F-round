// uniqueSortedNumbers
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/general/array.js, line 46
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const uniqueSortedNumbers = (array) => {
	// values are coerced into numbers (as the previous implementation did,
	// via object keys), so "4" or [4] become 4. object keys are only sorted
	// numerically for non-negative integers, floats and negative numbers
	// would remain in insertion order, so sort. (forEach skips array holes)
	const numbers = [];
	array.forEach((n) => numbers.push(parseFloat(String(n))));
	return Array.from(new Set(numbers)).sort((a, b) => a - b);
};
