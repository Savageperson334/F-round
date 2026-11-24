// setTextSize
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/drawing/drawingActions.js, line 34
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const SET_TEXT_SIZE = 'SET_TEXT_SIZE';


const setTextSize = (size) => {
    return {
        type: SET_TEXT_SIZE,
        value: size
    };
};
