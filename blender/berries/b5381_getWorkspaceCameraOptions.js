// getWorkspaceCameraOptions
//
// Copied verbatim from https://github.com/microsoft/haste
//   file ui/src/Components/LabelingTool/labelingToolLoading.js, line 25
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Satellites and orbital systems
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function getWorkspaceCameraOptions(bounds) {
  return {
    ...(bounds ? { bounds, padding: 24 } : {}),
    bearing: 0,
    pitch: 0,
    duration: 0,
  };
}
