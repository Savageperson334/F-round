// basisVectors
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/math/vector.js, line 557
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const magnitude2 = (v) => Math.sqrt(v[0] * v[0] + v[1] * v[1]);


const normalize2 = (v) => {
	const m = magnitude2(v);
	return m === 0 ? [v[0], v[1]] : [v[0] / m, v[1] / m];
};


const rotate90 = (v) => [-v[1], v[0]];


const basisVectors2 = (vector = [1, 0]) => {
	const normalized = normalize2(vector);
	return [normalized, rotate90(normalized)];
};


const magnitude3 = (v) => Math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2]);


const normalize3 = (v) => {
	const m = magnitude3(v);
	return m === 0 ? [v[0], v[1], v[2]] : [v[0] / m, v[1] / m, v[2] / m];
};


const cross3 = (v, u) => [
	v[1] * u[2] - v[2] * u[1],
	v[2] * u[0] - v[0] * u[2],
	v[0] * u[1] - v[1] * u[0],
];


const basisVectors3 = (vector = [1, 0, 0]) => {
	const normalized = normalize3(vector);

	// find a good candidate for a second basis vector
	/** @type {[number, number, number][]} */
	const candidates = [
		[1, 0, 0],
		[0, 1, 0],
		[0, 0, 1],
	];
	const crosses = candidates.map((v) => cross3(v, normalized));

	// before normalizing the cross products, find the result with
	// the largest magnitude, use this for the second basis vector
	const index = crosses
		.map(magnitude3)
		.map((n, i) => ({ n, i }))
		.sort((a, b) => b.n - a.n)
		.map((el) => el.i)
		.shift();

	// normalize the second basis vector
	const perpendicular = normalize3(crosses[index]);

	// the third basis vector is the cross product of the previous two
	return [normalized, perpendicular, cross3(normalized, perpendicular)];
};


const basisVectors = (vector) =>
	vector.length === 2
		? basisVectors2([vector[0], vector[1]])
		: basisVectors3([vector[0], vector[1], vector[2]]);
