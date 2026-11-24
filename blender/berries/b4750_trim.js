// trim
//
// Copied verbatim from https://github.com/almende/chap-links-library
//   file js/src/graph3d/playground/playground.js, line 443
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Graphs and networks
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function trim(text) {
    while (text.length && text.charAt(0) == ' ')
        text = text.substr(1);

    while (text.length && text.charAt(text.length-1) == ' ')
        text = text.substr(0, text.length-1);

    return text;
}
