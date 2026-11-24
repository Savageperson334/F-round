// setPlotSettingByKey
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/plot/plotActions.js, line 9
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const SET_PLOT_SETTING_BY_KEY = 'SET_PLOT_SETTING_BY_KEY';


const setPlotSettingByKey = (key, value) => {
    return {
        type: SET_PLOT_SETTING_BY_KEY,
        value: { key, value }
    };
};
