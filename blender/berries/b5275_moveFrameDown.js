// moveFrameDown
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/gifmaker/gifmakerActions.js, line 52
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const MOVE_FRAME_DOWN = 'MOVE_FRAME_DOWN';


const moveFrameDown = (id) => {
    return { type: MOVE_FRAME_DOWN, value: id };
};
