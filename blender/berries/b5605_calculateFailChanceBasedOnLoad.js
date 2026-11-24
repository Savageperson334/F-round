// calculateFailChanceBasedOnLoad
//
// Copied verbatim from https://github.com/pshenok/server-survival
//   file src/core/actions.js, line 489
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Public transport and city motion
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function calculateFailChanceBasedOnLoad(load) {
    if (load <= 0.5) return 0;
    return 2 * (load - 0.5);
}
