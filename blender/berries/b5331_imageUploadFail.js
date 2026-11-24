// imageUploadFail
//
// Copied verbatim from https://github.com/magicshifter/ms4000
//   file web/app/src/actions/ms3000.js, line 24
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const IMAGE_UPLOAD_REQUEST_FAIL = "IMAGE_UPLOAD_REQUEST_FAIL"


const imageUploadFail = (error) => ({
  type: IMAGE_UPLOAD_REQUEST_FAIL,
  error
})
