// pairwiseReferenceTest
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/graph/validate/validateReflexive.js, line 10
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const pairwiseReferenceTest = (a_b, b_a, aName, bName) => {
	try {
		// when we iterate through each array at its second level depth, we need
		// to be sure to filter out any null or undefined, as for example it's
		// requird by the spec to include undefined inside of vertices_faces,
		// but only inside the inner arrays. at the top level no nulls should exist.
		const abHash = {};
		a_b.forEach((_, a) => {
			abHash[a] = {};
		});
		a_b.forEach((arr, a) =>
			arr
				.filter((el) => el !== null && el !== undefined)
				.forEach((b) => {
					abHash[a][b] = true;
				}),
		);

		const baHash = {};
		b_a.forEach((_, b) => {
			baHash[b] = {};
		});
		b_a.forEach((arr, b) =>
			arr
				.filter((el) => el !== null && el !== undefined)
				.forEach((a) => {
					baHash[b][a] = true;
				}),
		);

		const abErrors = a_b.flatMap((arr, a) =>
			arr
				.filter((el) => el !== null && el !== undefined)
				.map((b) =>
					!baHash[b] || !baHash[b][a]
						? `${bName}_${aName}[${b}] missing ${a} referenced in ${aName}_${bName}`
						: undefined,
				)
				.filter((el) => el !== undefined),
		);
		const baErrors = b_a.flatMap((arr, b) =>
			arr
				.filter((el) => el !== null && el !== undefined)
				.map((a) =>
					!abHash[a] || !abHash[a][b]
						? `${aName}_${bName}[${a}] missing ${b} referenced in ${bName}_${aName}`
						: undefined,
				)
				.filter((el) => el !== undefined),
		);

		return abErrors.concat(baErrors);
	} catch (error) {
		return ["pairwise reference validation failed due to bad index access"];
	}
};
