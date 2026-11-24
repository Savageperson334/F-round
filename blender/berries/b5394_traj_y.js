// traj_y
//
// Copied verbatim from https://github.com/movsim/traffic-simulation-de
//   file js/coffeemeterGame.js, line 169
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Public transport and city motion
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

var yBegin=0;

var lenStraightBegin=600;

var maxAng=0.2;

var noCurves=(Math.abs(maxAng)<0.001);

var lenCurve=200;

var curvature=maxAng/lenCurve;

var u1=lenStraightBegin;

var u2=lenStraightBegin+lenCurve;

var u3=lenStraightBegin+2*lenCurve;


function traj_y(u){ 
    var y1=yBegin+lenStraightBegin;
    var y2=(noCurves) ? y1+lenCurve : y1+Math.sin(maxAng)/curvature;
    var y3=2*y2-y1;

    var y=(noCurves||(u<u1))
	? yBegin + u : (u<u2)
	? y1+Math.sin(maxAng*(u-u1)/(u2-u1))/curvature : (u<u3)
	? y3-Math.sin(maxAng*(u3-u)/(u3-u2))/curvature : y3+u-u3;
    return y;
}
