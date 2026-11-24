// duplicateLayer
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/layer/layerActions.js, line 70
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const DUPLICATE_LAYER = 'DUPLICATE_LAYER';


const duplicateLayer = (originalLayerID, newLayerID) => {
    return {
        type: DUPLICATE_LAYER,
        value: { originalLayerID, newLayerID }
    };
};
