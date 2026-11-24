// LagStep
//
// Copied verbatim from https://github.com/stoatworks-labs/ferrofluid
//   file demo/plugin.js, line 472
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ferrofluids and magnetic materials
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function LagStep(current, target, dt, tau) {
  if (dt <= 0.0) return current;
  if (tau <= 0.0) return target;
  return target + (current - target) * Math.exp(-dt / tau);
}
