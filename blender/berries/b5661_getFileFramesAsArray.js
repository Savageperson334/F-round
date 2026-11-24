// getFileFramesAsArray
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/fold/frames.js, line 96
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const getFileFramesAsArray = (graph) => {
	if (!graph) {
		return [];
	}
	if (!graph.file_frames || !graph.file_frames.length) {
		return [graph];
	}
	const frame0 = { ...graph };
	delete frame0.file_frames;
	return [frame0, ...graph.file_frames];
};
