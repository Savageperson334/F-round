// setRecording
//
// Copied verbatim from https://github.com/experimentalDataAesthetics/play-splom
//   file app/actions/transport.js, line 18
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Sound sonification
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function setRecording(recording) {
  // calls to the engine to start/stop recording
  // dispatches to set recording state
  return {
    type: 'setRecording',
    payload: {
      recording
    }
  };
}
