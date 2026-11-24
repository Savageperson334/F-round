// flattenDomTree
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/svg/general/dom.js, line 91
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const flattenDomTree = (el) =>
	el.childNodes == null || !el.childNodes.length
		? [el]
		: Array.from(el.childNodes).flatMap((child) => flattenDomTree(child));
