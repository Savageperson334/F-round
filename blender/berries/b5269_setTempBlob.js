// setTempBlob
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/gifmaker/gifmakerActions.js, line 28
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const SET_TEMP_BLOB = 'SET_TEMP_BLOB';


const setTempBlob = (tempBlob) => {
    return { type: SET_TEMP_BLOB, value: tempBlob };
};
