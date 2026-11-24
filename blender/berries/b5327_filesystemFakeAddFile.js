// filesystemFakeAddFile
//
// Copied verbatim from https://github.com/magicshifter/ms4000
//   file web/app/src/actions/filesystem.js, line 8
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const FILESYSTEM_FAKE_ADD_FILE = "FILESYSTEM_FAKE_ADD_FILE"


const filesystemFakeAddFile = (name) => ({
  type: FILESYSTEM_FAKE_ADD_FILE,
  name
})
