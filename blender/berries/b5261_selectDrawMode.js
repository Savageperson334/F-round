// selectDrawMode
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/drawing/drawingActions.js, line 20
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const SELECT_DRAW_MODE = 'SELECT_DRAW_MODE';


const selectDrawMode = (mode) => {
    return {
        type: SELECT_DRAW_MODE,
        value: mode
    };
};
