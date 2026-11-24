// imageDownloadStart
//
// Copied verbatim from https://github.com/magicshifter/ms4000
//   file web/app/src/actions/ms3000.js, line 105
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const IMAGE_DOWNLOAD_REQUEST_START = "IMAGE_DOWNLOAD_REQUEST_START"


const imageDownloadStart = (name) => ({
  type: IMAGE_DOWNLOAD_REQUEST_START,
  name,
})
