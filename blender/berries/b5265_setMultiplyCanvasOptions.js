// setMultiplyCanvasOptions
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/drawing/drawingActions.js, line 48
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const SET_MULTIPLY_CANVAS_OPTIONS = 'SET_MULTIPLY_CANVAS_OPTIONS';


const setMultiplyCanvasOptions = (axis, multiplyFactor) => {
    return {
        type: SET_MULTIPLY_CANVAS_OPTIONS,
        value: { axis, multiplyFactor }
    };
};
