// ordersTest
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/graph/validate/validateOrders.js, line 11
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const ordersTest = (orders, name = "orders") => {
	// orders between two faces that are actually the same face
	const sameFaceOrders = orders
		.map(([a, b], i) => (a === b ? [a, b, i] : undefined))
		.filter((a) => a !== undefined)
		.map(([a, b, i]) => `${name} between the same face ${a}, ${b} at index ${i}`);
	const pairHash = {};
	const duplicateOrders = orders
		.filter(([a, b]) => {
			const key = a < b ? `${a} ${b}` : `${b} ${a}`;
			const isDuplicate = pairHash[key] === true;
			pairHash[key] = true;
			return isDuplicate;
		})
		.map(([a, b]) => `${name} duplicate orders found between faces ${a}-${b}`);
	return sameFaceOrders.concat(duplicateOrders);
};
