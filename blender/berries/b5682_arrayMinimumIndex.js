// arrayMinimumIndex
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/general/array.js, line 230
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const arrayMinimumIndex = (array, map) => {
	if (!array.length) {
		return undefined;
	}
	const arrayValues =
		typeof map === "function" ? array.map((value) => map(value)) : array;
	let index = 0;
	arrayValues.forEach((value, i, arr) => {
		if (value < arr[index]) {
			index = i;
		}
	});
	return index;
};
