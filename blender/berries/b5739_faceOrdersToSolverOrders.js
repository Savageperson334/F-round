// faceOrdersToSolverOrders
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/layer/general.js, line 167
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const faceOrdersToSolverOrders = (faceOrders, faces_winding) => {
	/** @type {{[key: string]: number}} */
	const solverOrders = {};

	// convert the value (1 or 2) into the faceOrder value (-1 or +1).
	faceOrders.forEach(([f, g, order]) => {
		if (order !== 1 && order !== -1) {
			return;
		}
		// according to the FOLD spec, for order [f, g, s]:
		// +1 indicates that face f lies above face g
		// −1 indicates that face f lies below face g
		// where "above" means on the side pointed to by g's normal vector,
		// and "below" means on the side opposite g's normal vector.
		const solution = faces_winding[g]
			? // convert a 1 into a 1, and a -1 into a 2
				(1 - order) / 2 + 1
			: // convert a 1 into a 2, and a -1 into a 1
				(order + 1) / 2 + 1;
		const key = f < g ? `${f} ${g}` : `${g} ${f}`;
		solverOrders[key] =
			f < g
				? solution
				: // faces are in reversed order. swap 1 and 2
					3 - solution;
	});

	return solverOrders;
};
