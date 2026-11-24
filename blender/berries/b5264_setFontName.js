// setFontName
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/drawing/drawingActions.js, line 41
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const SET_FONT_NAME = 'SET_FONT_NAME';


const setFontName = (fontName) => {
    return {
        type: SET_FONT_NAME,
        value: fontName
    };
};
