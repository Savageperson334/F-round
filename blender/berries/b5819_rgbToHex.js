// rgbToHex
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/svg/colors/convert.js, line 73
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const rgbToHex = (red, green, blue, alpha) => {
	/** @param {number} n */
	const to16 = (n) =>
		`00${Math.max(0, Math.min(Math.round(n), 255)).toString(16)}`.slice(-2);
	const hex = `#${[red, green, blue].map(to16).join("")}`;
	return alpha === undefined ? hex : `${hex}${to16(alpha * 255)}`;
};
