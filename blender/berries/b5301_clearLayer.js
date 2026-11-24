// clearLayer
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/line/lineActions.js, line 76
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const CLEAR_LAYER = 'CLEAR_LAYER';


const clearLayer = (layerID) => {
    return {
        type: CLEAR_LAYER,
        value: { layerID }
    };
};
