// radialSortUnitVectors2
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/general/sort.js, line 57
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const radialSortUnitVectors2 = (vectors) => {
	// we filter each vector into two categories based on the sign of the Y value
	// and later will sort the vectors within each category based on the X value.
	// we are storing the indices here, not the vectors themselves.
	const sidesVectors = [[], []];
	vectors.map((vec) => (vec[1] >= 0 ? 0 : 1)).forEach((s, v) => sidesVectors[s].push(v));

	// each side can be sorted by simply comparing the x value since these
	// vectors are normalized. decreasing or increasing, for +Y and -Y.
	const sorts = [
		/** @param {number} a @param {number} b */
		(a, b) => vectors[b][0] - vectors[a][0],
		/** @param {number} a @param {number} b */
		(a, b) => vectors[a][0] - vectors[b][0],
	];

	// now we can sort each side, and since the sides themselves are
	// already sorted counter-clockwise, the flattened list will be sorted.
	return sidesVectors.flatMap((indices, i) => indices.sort(sorts[i]));
};
