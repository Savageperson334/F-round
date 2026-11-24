// traj0_y
//
// Copied verbatim from https://github.com/movsim/traffic-simulation-de
//   file js/test4_doubleLoop.js, line 196
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Public transport and city motion
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

var center_yRel=-0.5;

var refSizePhys=200;

var center_yPhys=center_yRel*refSizePhys;

var radius=0.35*refSizePhys;


function traj0_y(u){ // physical coordinates
  return center_yPhys+radius*Math.sin(Math.PI+u/radius);
}
