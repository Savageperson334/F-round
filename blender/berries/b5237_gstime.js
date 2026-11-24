// gstime
//
// Copied verbatim from https://github.com/koansys/isat
//   file js/gstime.js, line 31
//   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
//   catalogue shelf: Satellites and orbital systems
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function gstime(jdut1) {
    var twopi      = 2.0 * Math.PI,
        deg2rad    = Math.PI / 180.0,
        tut1, temp;

    // ------------------------  implementation   ------------------
    tut1 = (jdut1 - 2451545.0) / 36525.0;

    temp = -6.2e-6 * tut1 * tut1 * tut1 + 0.093104 * tut1 * tut1 +
        (876600.0 * 3600.0 + 8640184.812866) * tut1 + 67310.54841;

    // 360/86400 = 1/240, to deg, to rad
    temp = (temp * deg2rad / 240.0) % twopi;

    // ------------------------ check quadrants --------------------
    if (temp < 0.0) {
        temp = temp + twopi;
    }
    return temp;
}
