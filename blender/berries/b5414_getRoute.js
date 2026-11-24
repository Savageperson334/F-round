// getRoute
//
// Copied verbatim from https://github.com/movsim/traffic-simulation-de
//   file js/test4_doubleLoop.js, line 257
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Public transport and city motion
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function getRoute(routes,fracOff){
  var rnd=Math.random();
  return (rnd<1-fracOff) ? routes[0] : routes[1];
}
