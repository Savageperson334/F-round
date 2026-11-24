// moveFrameUp
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/gifmaker/gifmakerActions.js, line 48
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const MOVE_FRAME_UP = 'MOVE_FRAME_UP';


const moveFrameUp = (id) => {
    return { type: MOVE_FRAME_UP, value: id };
};
