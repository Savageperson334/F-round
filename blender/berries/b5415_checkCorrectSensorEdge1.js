// checkCorrectSensorEdge1
//
// Copied verbatim from https://github.com/movsim/traffic-simulation-de
//   file js/transform3d.js, line 212
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Public transport and city motion
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function checkCorrectSensorEdge1(nShoot,e1SensorIn){
    var e1Sensor=[];
    for (var i=0; i<3; i++){ // deep copying
	e1Sensor[i]=e1SensorIn[i];
    }
    
    var res=nShoot[0]*e1Sensor[0]+nShoot[1]*e1Sensor[1]+nShoot[2]*e1Sensor[2];
    if(Math.abs(res)>1e-6){
	var imax=0;
	var absmax=Math.abs(nShoot[0]);
	for(var i=1; i<3; i++){
	    if(Math.abs(nShoot[i])>absmax){
		imax=i;
		absmax=Math.abs(nShoot[i]);
	    }
	}
	e1Sensor[imax] -= res/nShoot[imax];
	console.log("checkCorrectSensorEdge1: camera edge e1sensor was not",
		    " perpendicular to nShoot.",
		    "\n corrected component ",imax,
		    " by an amount ", -res/nShoot[imax],
                    " resulting in",
		    "\n  ",e1Sensor);
    }

    // normalize e1Sensor and return

    var norm=Math.sqrt(e1Sensor[0]*e1Sensor[0]+e1Sensor[1]*e1Sensor[1]
		       +e1Sensor[2]*e1Sensor[2]);
    for(var i=0; i<3; i++){
	e1Sensor[i]=e1Sensor[i]/=norm;
    }

    return e1Sensor;
}
