// setMasterGif
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/gifmaker/gifmakerActions.js, line 44
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const SET_MASTER_GIF = 'SET_MASTER_GIF';


const setMasterGif = (masterGif) => {
    return { type: SET_MASTER_GIF, value: masterGif };
};
