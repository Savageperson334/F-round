// nonUniqueElements
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/general/array.js, line 28
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const nonUniqueElements = (array) => {
	const count = {};
	array.forEach((el) => {
		if (count[el] === undefined) {
			count[el] = 0;
		}
		count[el] += 1;
	});
	return array.filter((el) => count[el] > 1);
};
