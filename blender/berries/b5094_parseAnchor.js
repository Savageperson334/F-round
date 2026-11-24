// parseAnchor
//
// Copied verbatim from https://github.com/hazymorning/origami_weather
//   file src/origami-weather.js, line 1570
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function parseAnchor(anchor) {
    if (anchor === 'center' || anchor === 'left' || anchor === 'right') return ['center', anchor];
    return anchor.includes('-') ? anchor.split('-') : ['top', anchor];
}
