// configDownloadFail
//
// Copied verbatim from https://github.com/magicshifter/ms4000
//   file web/app/src/actions/ms3000.js, line 217
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const CONFIG_DOWNLOAD_REQUEST_FAIL = "CONFIG_DOWNLOAD_REQUEST_FAIL"


const configDownloadFail = (error) => ({
  type: CONFIG_DOWNLOAD_REQUEST_FAIL,
  error
})
