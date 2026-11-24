// fnc_rand
//
// Copied verbatim from https://github.com/arf-berkeley/architecture
//   file juliamorgan/js/qgis2web_expressions.js, line 102
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function fnc_rand(values, context) {
    return Math.floor(Math.random()*(values[1]-values[0]+1)+values[0]);
}
