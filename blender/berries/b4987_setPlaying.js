// setPlaying
//
// Copied verbatim from https://github.com/experimentalDataAesthetics/play-splom
//   file app/actions/transport.js, line 4
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Sound sonification
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function setPlaying(playing) {
  // calls to the engine to start
  // dispatches to set playing
  return {
    type: 'setPlaying',
    payload: {
      playing
    }
  };
}
