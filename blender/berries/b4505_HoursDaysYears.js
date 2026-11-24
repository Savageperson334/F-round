// HoursDaysYears
//
// Copied verbatim from https://github.com/Simone-Dr/SolarSystem
//   file sketch.js, line 491
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function HoursDaysYears(days){ 
	
	let str = "";

	if (days >= 365){
		let y = Math.floor(days/365);
		if (y == 1) {str += y + " year";}
		else {str += y + " years";}

		let d = Math.round((days % 365) * 100) / 100 ;
		if (d == 1) {str += ", " + d + " day ";}
		else if (d != 0 && d != 1) { str += ", " +  d + " days ";}
		return (str);
	}

	if (days < 365) {

		let d = Math.floor(days);

		if (d == 1) {str += (d + " day"); }
		else if (d != 0 && d != 1) {str += (d + " days");}


		let h = Math.round((days - d) * 24 * 100) / 100;

		if (d != 0 && h!= 0) {str += ", "; }
		if (h != 0) { str +=  h + " hours ";}

		return (str);
	}

}
