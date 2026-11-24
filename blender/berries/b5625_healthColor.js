// healthColor
//
// Copied verbatim from https://github.com/pshenok/server-survival
//   file src/ui/metrics-panel.js, line 73
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Public transport and city motion
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function healthColor(health) {
    return health < 40 ? "text-red-400" : health < 70 ? "text-yellow-400" : "text-green-400";
}
