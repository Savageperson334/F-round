// moveLayerUp
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/layer/layerActions.js, line 49
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const MOVE_LAYER_UP = 'MOVE_LAYER_UP';


const moveLayerUp = (layerID) => {
    return {
        type: MOVE_LAYER_UP,
        value: layerID
    };
};
