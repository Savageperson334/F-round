// parseJsonOrNull
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/services/config/parseUploadedMusicBoxConfig.js, line 38
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const parseJsonOrNull = (text) => {
  try {
    return JSON.parse(text)
  } catch (_error) {
    return null
  }
}
