// smoothTowardsRPS
//
// Copied verbatim from https://github.com/pshenok/server-survival
//   file game.js, line 157
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Public transport and city motion
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function smoothTowardsRPS(current, target, dt) {
    return current + (target - current) * (1 - Math.pow(0.99, dt * 60));
}
