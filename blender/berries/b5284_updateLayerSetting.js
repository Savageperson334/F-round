// updateLayerSetting
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/store/layer/layerActions.js, line 42
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const UPDATE_LAYER_SETTING = 'UPDATE_LAYER_SETTING';


const updateLayerSetting = (layerID, settingKey, settingValue) => {
    return {
        type: UPDATE_LAYER_SETTING,
        value: { layerID, settingKey, settingValue }
    };
};
