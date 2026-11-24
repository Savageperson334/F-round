// configUploadFail
//
// Copied verbatim from https://github.com/magicshifter/ms4000
//   file web/app/src/actions/ms3000.js, line 158
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const CONFIG_UPLOAD_REQUEST_FAIL = "CONFIG_UPLOAD_REQUEST_FAIL"


const configUploadFail = (error) => ({
  type: CONFIG_UPLOAD_REQUEST_FAIL,
  error
})
