// addFilterToLayerByID
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/layer/layerActions.js, line 79
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const ADD_FILTER_TO_LAYER_BY_ID = 'ADD_FILTER_TO_LAYER_BY_ID';


const addFilterToLayerByID = (layerID, filterSettings) => {
    return {
        type: ADD_FILTER_TO_LAYER_BY_ID,
        value: { layerID, filterSettings }
    };
};
