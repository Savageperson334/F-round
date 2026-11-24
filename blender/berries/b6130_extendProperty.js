// extendProperty
//
// Copied verbatim from https://github.com/wsldl123292/Origami
//   file src/main/webapp/ueditor/dialogs/wordimage/wordimage.js, line 112
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function extendProperty(fromObj, toObj) {
	for (var i in fromObj) {
		if (!toObj[i]) {
			toObj[i] = fromObj[i];
		}
	}
	return toObj;
}
