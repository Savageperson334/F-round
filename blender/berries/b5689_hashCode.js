// hashCode
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/general/hashCode.js, line 18
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const hashCode = (string) => {
	let hash = 0;
	for (let i = 0; i < string.length; i += 1) {
		hash = (hash << 5) - hash + string.charCodeAt(i);
		hash |= 0; // Convert to 32bit integer
	}
	return hash;
};
