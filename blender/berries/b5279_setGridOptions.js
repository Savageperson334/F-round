// setGridOptions
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/global/globalActions.js, line 20
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const SET_GRID_OPTIONS = 'SET_GRID_OPTIONS';


const setGridOptions = (options) => {
    return { type: SET_GRID_OPTIONS, value: options };
};
