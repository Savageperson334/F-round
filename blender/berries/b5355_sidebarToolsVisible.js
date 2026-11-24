// sidebarToolsVisible
//
// Copied verbatim from https://github.com/magicshifter/ms4000
//   file web/app/src/actions/sidebar.js, line 11
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const SIDEBAR_TOOLS_VISIBLE = "SIDEBAR_TOOLS_VISIBLE"


const sidebarToolsVisible = (toolsVisible) => ({
  type: SIDEBAR_TOOLS_VISIBLE,
  toolsVisible
})
