// connectedComponentsPairs
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/graph/connectedComponents.js, line 67
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const connectedComponentsPairs = (array_array) => {
	const pairs = [];

	// if a component's index is self-adjacent, this functions as a hash
	// lookup to ensure that the reference appears only once.
	const circular = [];
	array_array.forEach((arr, i) =>
		arr.forEach((j) => {
			// assuming that i exists in j's adjacent, and visa versa, we will visit
			// every permutation twice. only include the one where i < j.
			if (i < j) {
				pairs.push([i, j]);
			}

			// if an index is self-referential, ensure that it is only added once
			if (i === j && !circular[i]) {
				circular[i] = true;
				pairs.push([i, j]);
			}
		}),
	);
	return pairs;
};
