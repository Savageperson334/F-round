// selectMainMode
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/drawing/drawingActions.js, line 13
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const SELECT_MAIN_MODE = 'SELECT_MAIN_MODE';


const selectMainMode = (mode) => {
    return {
        type: SELECT_MAIN_MODE,
        value: mode
    };
};
