// addActiveFrame
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/gifmaker/gifmakerActions.js, line 40
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const ADD_ACTIVE_FRAME = 'ADD_ACTIVE_FRAME';


const addActiveFrame = (frame) => {
    return { type: ADD_ACTIVE_FRAME, value: frame };
};
