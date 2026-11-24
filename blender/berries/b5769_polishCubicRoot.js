// polishCubicRoot
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/math/polynomial.js, line 23
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const polishCubicRoot = (a0, a1, a2, root) => {
	let x = root;
	let f = ((x + a2) * x + a1) * x + a0;
	for (let i = 0; i < 4; i += 1) {
		const df = (3 * x + 2 * a2) * x + a1;
		if (Math.abs(df) < 1e-12) {
			break;
		}
		// near a double root the derivative is near 0 and a Newton step
		// can overshoot, only accept a step if it brings us closer to 0.
		const next = x - f / df;
		const nextF = ((next + a2) * next + a1) * next + a0;
		if (Math.abs(nextF) >= Math.abs(f)) {
			break;
		}
		x = next;
		f = nextF;
	}
	return x;
};
