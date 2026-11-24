// setVisibilityForAllLayers
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/layer/layerActions.js, line 38
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const SET_VISIBILITY_FOR_ALL_LAYERS = 'SET_VISIBILITY_FOR_ALL_LAYERS';


const setVisibilityForAllLayers = (visible) => {
    return { type: SET_VISIBILITY_FOR_ALL_LAYERS, value: visible };
};
