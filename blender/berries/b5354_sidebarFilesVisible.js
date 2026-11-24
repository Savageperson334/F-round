// sidebarFilesVisible
//
// Copied verbatim from https://github.com/magicshifter/ms4000
//   file web/app/src/actions/sidebar.js, line 6
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const SIDEBAR_FILES_VISIBLE = "SIDEBAR_FILES_VISIBLE"


const sidebarFilesVisible = (filesVisible) => ({
  type: SIDEBAR_FILES_VISIBLE,
  filesVisible
})
