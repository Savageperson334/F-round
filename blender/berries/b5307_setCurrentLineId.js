// setCurrentLineId
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/plot/plotActions.js, line 23
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const SET_CURRENT_LINE_ID = 'SET_CURRENT_LINE_ID';


const setCurrentLineId = (lineId) => {
    return {
        type: SET_CURRENT_LINE_ID,
        value: lineId
    };
};
