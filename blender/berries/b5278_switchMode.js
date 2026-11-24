// switchMode
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/global/globalActions.js, line 8
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const SWITCH_MODE = 'SWITCH_MODE';


const switchMode = (mode) => {
    return { type: SWITCH_MODE, value: mode };
};
