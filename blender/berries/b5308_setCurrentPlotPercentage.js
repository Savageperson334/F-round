// setCurrentPlotPercentage
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/plot/plotActions.js, line 30
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const SET_CURRENT_PLOT_PERCENTAGE = 'SET_CURRENT_PLOT_PERCENTAGE';


const setCurrentPlotPercentage = (percentage) => {
    return {
        type: SET_CURRENT_PLOT_PERCENTAGE,
        value: percentage
    };
};
