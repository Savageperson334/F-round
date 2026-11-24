// foldFacesLayer
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/graph/fold/flatFold.js, line 616
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const foldFacesLayer = (faces_layer, faces_folding) => {
	const new_faces_layer = [];
	// filter face indices into two arrays, those folding and not folding
	const arr = faces_layer.map((_, i) => i);
	const folding = arr.filter((i) => faces_folding[i]);
	const not_folding = arr.filter((i) => !faces_folding[i]);
	// sort all the non-folding indices by their current layer, bottom to top,
	// give each face index a new layering index.
	// compress whatever current layer numbers down into [0...n]
	not_folding
		.sort((a, b) => faces_layer[a] - faces_layer[b])
		.forEach((face, i) => {
			new_faces_layer[face] = i;
		});
	// sort the folding faces in reverse order (flip them), compress their
	// layers down into [0...n] and and set each face to this layer index
	folding
		.sort((a, b) => faces_layer[b] - faces_layer[a]) // reverse order here
		.forEach((face, i) => {
			new_faces_layer[face] = not_folding.length + i;
		});
	return new_faces_layer;
};
