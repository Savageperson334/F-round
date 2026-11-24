// configUpdate
//
// Copied verbatim from https://github.com/magicshifter/ms4000
//   file web/app/src/actions/ms3000.js, line 262
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const CONFIG_UPDATE = 'CONFIG_UPDATE'


const configUpdate = (shifterState) => ({
  type: CONFIG_UPDATE,
  shifterState,
})
