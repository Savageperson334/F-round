// newtonnu
//
// Copied verbatim from https://github.com/koansys/isat
//   file js/isat.js, line 1196
//   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
//   catalogue shelf: Satellites and orbital systems
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function asinh(val) {
    'use strict';
    return Math.log(val + Math.sqrt(val * val + 1));
}


function sinh(val) {
    'use strict';
    return (Math.pow(Math.E, val) - Math.pow(Math.E, -val)) / 2;
}


function newtonnu(ecc, nu) {
    'use strict';
    var e0 = 999999.9,
        m = 999999.9,
        small = 0.00000001,
        sine, cose;

    // --------------------------- circular ------------------------
    if (Math.abs(ecc) < small) {
        m  = nu;
        e0 = nu;
    }
    else {
        // ---------------------- elliptical -----------------------
        if (ecc < 1.0 - small) {
            sine = (Math.sqrt(1.0 - ecc * ecc) * Math.sin(nu)) / (1.0 + ecc * Math.cos(nu));
            cose = (ecc + Math.cos(nu)) / (1.0 + ecc * Math.cos(nu));
            e0  = Math.atan2(sine, cose);
            m   = e0 - ecc * Math.sin(e0);
        }
        else {
            // -------------------- hyperbolic  --------------------
            if (ecc > 1.0 + small) {
                if ((ecc > 1.0) &&
                    (Math.abs(nu) + 0.00001 < Math.PI - Math.acos(1.0 / ecc))) {
                    sine = (Math.sqrt(ecc * ecc - 1.0) * Math.sin(nu)) / (1.0 + ecc * Math.cos(nu));
                    e0   = asinh(sine);
                    m    = ecc * sinh(e0) - e0;
                }
                else {
                    // ----------------- parabolic ---------------------
                    if (Math.abs(nu) < 168.0 * Math.PI / 180.0) {
                        e0 = Math.tan(nu * 0.5);
                        m  = e0 + (e0 * e0 * e0) / 3.0;
                    }
                }
            }
        }
    }


    if (ecc < 1.0) {
        m = m % (2.0 * Math.PI);
        if (m < 0.0) {
            m = m + 2.0 * Math.PI;
        }
        e0 = e0 % (2.0 * Math.PI);
    }

    return [e0, m];
}
