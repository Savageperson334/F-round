// deleteLibraryFrame
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/gifmaker/gifmakerActions.js, line 20
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const DELETE_LIBRARY_FRAME = 'DELETE_LIBRARY_FRAME';


const deleteLibraryFrame = (frameID) => {
    return { type: DELETE_LIBRARY_FRAME, value: frameID };
};
