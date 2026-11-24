// clustersToReflexiveArrays
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/general/array.js, line 299
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const chooseTwoPairs = (array) => {
	const pairs = Array((array.length * (array.length - 1)) / 2);
	let index = 0;
	for (let i = 0; i < array.length - 1; i += 1) {
		for (let j = i + 1; j < array.length; j += 1, index += 1) {
			pairs[index] = [array[i], array[j]];
		}
	}
	return pairs;
};


const clustersToReflexiveArrays = (clusters) => {
	const result = [];
	clusters.flat().forEach((i) => {
		result[i] = [];
	});
	clusters.flatMap(chooseTwoPairs).forEach(([a, b]) => {
		result[a].push(b);
		result[b].push(a);
	});
	return result;
};
