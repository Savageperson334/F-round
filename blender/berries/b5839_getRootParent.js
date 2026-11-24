// getRootParent
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/svg/general/dom.js, line 26
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const getRootParent = (el) => {
	/** @type {Element} */
	let parent = el;
	while (parent && parent.parentElement != null) {
		parent = parent.parentElement;
	}
	return parent;
};
