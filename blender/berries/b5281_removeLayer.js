// removeLayer
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/layer/layerActions.js, line 30
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const REMOVE_LAYER = 'REMOVE_LAYER';


const removeLayer = (layerId) => {
    return { type: REMOVE_LAYER, value: layerId };
};
