// traj1_y
//
// Copied verbatim from https://github.com/movsim/traffic-simulation-de
//   file js/test4_doubleLoop.js, line 209
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Public transport and city motion
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

var refSizePhys=200;

var lenStraight=0.20*refSizePhys;

var center_yRel=-0.5;

var center_yPhys=center_yRel*refSizePhys;

var radius=0.35*refSizePhys;

var lenHalfRing=Math.PI*radius+2*lenStraight;


function traj1_y(u){ 
  return (u<lenStraight)
    ? center_yPhys-radius : (u<lenHalfRing-lenStraight)
    ? center_yPhys+radius*Math.sin(1.5*Math.PI+(u-lenStraight)/radius)
    : center_yPhys+radius;
}
