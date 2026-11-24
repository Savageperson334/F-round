// getCorsFreeUrl
//
// Copied verbatim from https://github.com/dsuarezv/satellite-tracker
//   file samples/iss-1day/index.js, line 4
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Satellites and orbital systems
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function getCorsFreeUrl(url) {
    return 'https://cors-anywhere.herokuapp.com/' + url;
}
