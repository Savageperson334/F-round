// navigationSetLocation
//
// Copied verbatim from https://github.com/magicshifter/ms4000
//   file web/app/src/actions/navigation.js, line 3
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const NAVIGATION_SET_LOCATION = 'NAVIGATION_SET_LOCATION'


const navigationSetLocation = (location) => ({
  type: NAVIGATION_SET_LOCATION,
  location
})
