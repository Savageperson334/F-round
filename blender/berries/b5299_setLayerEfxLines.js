// setLayerEfxLines
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/line/lineActions.js, line 43
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const SET_LAYER_EFX_LINES = 'SET_LAYER_EFX_LINES';


const setLayerEfxLines = (layerID, efxLines) => {
    return {
        type: SET_LAYER_EFX_LINES,
        value: { layerID, efxLines }
    };
};
