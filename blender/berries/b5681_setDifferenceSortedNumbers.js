// setDifferenceSortedNumbers
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/general/array.js, line 169
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const setDifferenceSortedNumbers = (a, b) => {
	const result = [];
	let ai = 0;
	let bi = 0;
	if (!b.length) {
		return a.slice();
	}
	while (ai < a.length && bi < b.length) {
		if (a[ai] === b[bi]) {
			ai += 1;
		} else if (a[ai] > b[bi]) {
			bi += 1;
		} else if (b[bi] > a[ai]) {
			result.push(a[ai]);
			ai += 1;
		}
	}
	// once "b" is exhausted, all remaining values in "a" are kept
	return result.concat(a.slice(ai));
};
