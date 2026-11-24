// alternatingSumDifference
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/singleVertex/kawasaki.js, line 33
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const alternatingSum = (numbers) =>
	[0, 1].map((even_odd) =>
		numbers.filter((_, i) => i % 2 === even_odd).reduce((a, b) => a + b, 0),
	);


const alternatingSumDifference = (sectors) => {
	const halfsum = sectors.reduce((a, b) => a + b, 0) / 2;
	return alternatingSum(sectors).map((s) => s - halfsum);
};
